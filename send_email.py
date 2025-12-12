# -*- coding: utf-8 -*-
# @Author  : HeLei
# @Time    : 2025/12/12 16:49
# @File    : email.py
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 邮件配置
sender_email = "johnfash86@gmail.com"  # 你的 Gmail 地址
sender_password = "blfmtukzwgshgcgi"  # Gmail 应用专用密码（非普通密码）
receiver_email = "qq905713813@163.com"  # 163 收件人地址
smtp_server = "smtp.gmail.com"  # Gmail SMTP 服务器
smtp_port = 587  # 端口

# 邮件内容
subject = "测试邮件 - 从 Gmail 到 163"  # 主题
body = "这是一封从 Google 邮箱发送到 163 邮箱的测试邮件！"  # 正文

# 创建 MIMEText 对象
msg = MIMEText(body, 'plain', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = sender_email
msg['To'] = receiver_email

try:
    # 连接并发送
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # 启用 TLS 加密
    server.login(sender_email, sender_password)

    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("邮件发送成功！请检查 163 邮箱。")

except Exception as e:
    print(f"发送失败：{e}")

finally:
    server.quit()