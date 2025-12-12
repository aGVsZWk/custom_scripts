# -*- coding: utf-8 -*-
# @Author  : HeLei
# @Time    : 2025/12/12 16:44
# @File    : manager.py
import schedule
import time
import logging
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import json


class AutomationManager:
    def __init__(self, config_file='config.json'):
        self.config = self.load_config(config_file)
        self.setup_logging()

    def load_config(self, config_file):
        """加载配置文件"""
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                'monitoring': {'interval': 300},
                'alerts': {'enabled': True},
                'backup': {'enabled': False}
            }

    def setup_logging(self):
        """配置日志系统"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('automation.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def schedule_tasks(self):
        """安排定时任务"""
        # 每日数据采集任务
        schedule.every().day.at("02:00").do(self.daily_crawl_task)

        # 每小时健康检查
        schedule.every().hour.do(self.health_check)

        # 每30分钟监控数据质量
        schedule.every(30).minutes.do(self.data_quality_check)

    def daily_crawl_task(self):
        """每日爬虫任务"""
        self.logger.info("开始执行每日爬虫任务")

        try:
            # 执行爬虫逻辑
            crawler = AdvancedCrawler(self.config['target_url'])
            results = crawler.crawl_sitemap()

            # 数据验证
            if self.validate_data(results):
                self.backup_data(results)
                self.logger.info("每日爬虫任务完成")
            else:
                self.send_alert("数据验证失败", "采集的数据未通过质量检查")

        except Exception as e:
            self.logger.error(f"每日爬虫任务失败: {e}")
            self.send_alert("爬虫任务异常", str(e))

    def health_check(self):
        """系统健康检查"""
        checks = [
            self.check_database_connection,
            self.check_disk_space,
            self.check_network_status
        ]

        for check in checks:
            if not check():
                self.send_alert("系统健康检查失败", f"检查项 {check.__name__} 失败")

    def send_alert(self, subject, message):
        """发送告警通知"""
        if not self.config['alerts']['enabled']:
            return

        try:
            # 邮件告警配置
            msg = MIMEText(message, 'plain', 'utf-8')
            msg['Subject'] = subject
            msg['From'] = self.config['smtp']['from_addr']
            msg['To'] = ', '.join(self.config['alerts']['recipients'])

            with smtplib.SMTP(self.config['smtp']['server']) as server:
                server.login(self.config['smtp']['username'],
                             self.config['smtp']['password'])
                server.send_message(msg)

            self.logger.info(f"告警发送成功: {subject}")
        except Exception as e:
            self.logger.error(f"告警发送失败: {e}")

    def run(self):
        """启动自动化管理器"""
        self.logger.info("自动化管理器启动")
        self.schedule_tasks()

        while True:
            schedule.run_pending()
            time.sleep(1)


# 配置示例
config = {
    "target_url": "https://example.com",
    "monitoring": {"interval": 300},
    "alerts": {
        "enabled": True,
        "recipients": ["admin@example.com"]
    },
    "smtp": {
        "server": "smtp.example.com",
        "username": "alert@example.com",
        "password": "password",
        "from_addr": "alert@example.com"
    }
}

# 保存配置
with open('config.json', 'w') as f:
    json.dump(config, f, indent=2)

# 启动自动化系统
manager = AutomationManager()
manager.run()
