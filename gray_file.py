import cv2
import numpy as np
import os
import sys


def generate_sharp_optimized_image(image_path):
    """
    生成文字边缘锐利、无过度模糊的processed_image_optimized.jpg
    （解决粗/模糊问题，适配模板裁剪）
    """
    # 1. 检查图片路径
    if not os.path.exists(image_path):
        print(f"❌ 错误：图片 {image_path} 不存在！")
        return False

    # 2. 读取图片并统一通道
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if img is None:
        print(f"❌ 错误：无法读取图片 {image_path}！")
        return False

    # 补全通道数（仅做兼容，不影响清晰度）
    if len(img.shape) == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    elif len(img.shape) == 3 and img.shape[2] == 4:
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    # 3. 优化预处理：减少模糊，增强边缘（核心修改）
    # 缩放：使用更锐利的插值方式（INTER_LANCZOS4）
    h, w = img.shape[:2]
    scale = 1080 / max(h, w)
    img_scaled = cv2.resize(
        img, (int(w * scale), int(h * scale)),
        interpolation=cv2.INTER_LANCZOS4  # 最锐利的缩放方式，适合文字
    )

    # 转灰度图（保留原始对比度）
    img_gray = cv2.cvtColor(img_scaled, cv2.COLOR_BGR2GRAY)

    # 轻度对比度增强（避免过度）
    clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(16, 16))  # 降低增强强度，减少粗化
    img_gray = clahe.apply(img_gray)

    # 极小化降噪（仅过滤像素噪点，保留文字边缘）
    img_gray = cv2.GaussianBlur(img_gray, (1, 1), 0)  # 1x1核=无模糊，仅兼容接口

    # 边缘增强（关键：让文字边缘更锐利）
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])  # 锐化核
    img_gray = cv2.filter2D(img_gray, -1, kernel)

    # 二值化：手动阈值（避免OTSU过度粗化）
    # 可根据自己的截图调整阈值（150-200之间），数值越高文字越细
    _, img_bin = cv2.threshold(img_gray, 180, 255, cv2.THRESH_BINARY)

    # 4. 形态学细化（解决文字过粗问题）
    kernel = np.ones((1, 1), np.uint8)  # 1x1核=无腐蚀，如需更细可改为(2,2)
    img_bin = cv2.erode(img_bin, kernel, iterations=1)  # 轻度腐蚀，细化文字

    # 转为3通道保存（方便查看/裁剪）
    img_optimized = cv2.cvtColor(img_bin, cv2.COLOR_GRAY2BGR)

    # 5. 保存清晰的预处理图
    cv2.imwrite("processed_image_optimized.jpg", img_optimized)
    print(f"✅ 高清晰预处理图已生成：processed_image_optimized.jpg")
    print(f"📌 图片尺寸：{img_optimized.shape[1]}x{img_optimized.shape[0]}（宽x高）")
    print(f"💡 提示：若文字仍粗，可将代码中阈值180调高（如190），或把腐蚀核改为(2,2)")
    return True


# ========== 运行入口 ==========
if __name__ == "__main__":
    # 替换为你的截图路径（如img.png）
    IMAGE_PATH = "img.png"

    success = generate_sharp_optimized_image(IMAGE_PATH)

    if success:
        print("\n✅ 下一步操作：")
        print("1. 打开 processed_image_optimized.jpg，查看文字是否清晰锐利；")
        print("2. 若文字仍粗/模糊：")
        print("   - 调高大阈值（180→190/200）→ 文字变细；")
        print("   - 腐蚀核改为(2,2) → 进一步细化文字；")
        print("3. 裁剪图中的“复制”二字，保存为copy_template.jpg即可。")
    else:
        sys.exit(1)