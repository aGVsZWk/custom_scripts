import cv2
import numpy as np
import os
import sys
from PIL import Image, ImageDraw, ImageFont


def create_copy_template():
    """创建“复制”二字的模板图（不依赖cv2.freetype，兼容所有OpenCV版本）"""
    # ========== 第一步：用PIL绘制中文（PIL原生支持中文） ==========
    # 1. 创建PIL画布（黑色背景，尺寸(宽, 高)）
    width, height = 120, 60
    pil_img = Image.new('L', (width, height), 0)  # 'L'=灰度图，0=黑色

    # 2. 找到系统中文字体（兼容不同系统）
    font_paths = [
        # Mac
        "/System/Library/Fonts/PingFang.ttc",
        "/Library/Fonts/SimHei.ttf",
        # Windows
        "C:/Windows/Fonts/simhei.ttf",
        "C:/Windows/Fonts/msyh.ttc",
        # 通用备选（如果以上都找不到，手动指定）
        "SimHei.ttf"
    ]
    font_path = None
    for path in font_paths:
        if os.path.exists(path):
            font_path = path
            break

    if not font_path:
        print("⚠️ 未找到中文字体！请将SimHei.ttf（黑体）放到代码同目录")
        return None

    # 3. 加载字体并绘制“复制”
    try:
        # 加载字体（大小30，可调整）
        font = ImageFont.truetype(font_path, 30)
        # 创建绘制对象
        draw = ImageDraw.Draw(pil_img)
        # 绘制白色“复制”二字（位置可调整）
        draw.text((10, 10), "复制", font=font, fill=255)
    except Exception as e:
        print(f"❌ 绘制中文失败：{e}")
        return None

    # ========== 第二步：转为OpenCV格式并优化 ==========
    # PIL转OpenCV（灰度图）
    template = np.array(pil_img, dtype=np.uint8)

    # 轻度降噪+二值化（纯黑纯白）
    template = cv2.GaussianBlur(template, (1, 1), 0)
    _, template = cv2.threshold(template, 127, 255, cv2.THRESH_BINARY)

    # ========== 第三步：保存模板 ==========
    cv2.imwrite("copy_template.png", template)
    print("✅ 中文模板生成成功！文件：copy_template.png")
    return template

def find_copy_by_template(image_path):
    """
    用模板匹配定位“复制”二字（绕开OCR中文识别问题）
    """
    # 1. 检查图片路径
    if not os.path.exists(image_path):
        print(f"❌ 错误：图片 {image_path} 不存在！")
        return []

    # 2. 读取并预处理原始图片
    img = cv2.imread(image_path)
    if img is None:
        print(f"❌ 错误：无法读取图片 {image_path}！")
        return []

    # 统一转为3通道
    if len(img.shape) == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    elif len(img.shape) == 3 and img.shape[2] == 4:
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    # 转灰度图+二值化（和模板保持一致）
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img_bin = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # 3. 创建/读取“复制”模板
    if os.path.exists("copy_template.png"):
        template = cv2.imread("copy_template.png", 0)
    else:
        template = create_copy_template()

    # 4. 多尺度模板匹配（适配不同大小的“复制”文字）
    copy_positions = []
    h, w = template.shape[:2]
    # 缩放范围：0.5倍 ~ 2倍（覆盖常见的文字大小）
    for scale in np.linspace(0.5, 2.0, 20):
        # 缩放模板
        resized_template = cv2.resize(
            template, (int(w * scale), int(h * scale)),
            interpolation=cv2.INTER_CUBIC
        )
        th, tw = resized_template.shape[:2]
        if th > img_bin.shape[0] or tw > img_bin.shape[1]:
            continue

        # 执行匹配
        result = cv2.matchTemplate(img_bin, resized_template, cv2.TM_CCOEFF_NORMED)
        # 筛选匹配结果（阈值0.6，越高越精准）
        loc = np.where(result >= 0.6)

        # 收集匹配位置
        for pt in zip(*loc[::-1]):
            # 去重：避免同一位置被多次匹配
            is_duplicate = False
            for pos in copy_positions:
                if abs(pt[0] - pos["x"]) < tw / 2 and abs(pt[1] - pos["y"]) < th / 2:
                    is_duplicate = True
                    break
            if not is_duplicate:
                copy_positions.append({
                    "x": pt[0],
                    "y": pt[1],
                    "width": tw,
                    "height": th,
                    "confidence": round(result[pt[1], pt[0]], 2)
                })

    # 5. 可视化标注
    img_vis = img.copy()
    for pos in copy_positions:
        x, y = pos["x"], pos["y"]
        w, h = pos["width"], pos["height"]
        # 绘制红色矩形框
        cv2.rectangle(
            img_vis, (x, y), (x + w, y + h),
            (0, 0, 255), 2
        )
        # 标注“复制”
        cv2.putText(
            img_vis, "复制", (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2
        )

    cv2.imwrite("copy_result_final.jpg", img_vis)
    print(f"✅ 可视化结果已保存：copy_result_final.jpg")

    return copy_positions


# ========== 测试入口 ==========
if __name__ == "__main__":
    IMAGE_PATH = "img.png"  # 替换为你的截图路径
    if not os.path.exists(IMAGE_PATH):
        print(f"❌ 请先将截图保存为 {IMAGE_PATH}！")
        sys.exit(1)

    # 执行模板匹配
    positions = find_copy_by_template(IMAGE_PATH)

    # 输出结果
    if positions:
        print(f"\n🎉 成功找到「复制」共 {len(positions)} 处：")
        for idx, pos in enumerate(positions):
            lt = (pos["x"], pos["y"])
            rb = (pos["x"] + pos["width"], pos["y"] + pos["height"])
            print(f"  第{idx + 1}处：左上{lt}，右下{rb}，匹配度{pos['confidence']}")
    else:
        print("\n❌ 未找到「复制」，请检查：")
        print("1. 截图中的“复制”文字是否清晰、无严重变形；")
        print("2. 尝试调整代码中匹配阈值（0.6），调低到0.4试试；")
        print("3. 替换copy_template.jpg为你截图里的“复制”文字裁剪图；")
        print("4. 确保截图中的“复制”是简体、无特殊字体（如艺术字）。")