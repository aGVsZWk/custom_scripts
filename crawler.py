# -*- coding: utf-8 -*-
# @Author  : HeLei
# @Time    : 2025/12/12 16:01
# @File    : spider_template.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
import time
import requests
from urllib.parse import urljoin, urlparse
import random
import parser


class BasicCrawler:
    def __init__(self, base_url, delay=1):
        self.base_url = base_url
        self.delay = delay
        self.session = requests.Session()
        # 设置通用的请求头，模拟真实浏览器
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive'
        })

    def make_request(self, url, method='GET', **kwargs):
        """发送HTTP请求的基础方法"""
        full_url = urljoin(self.base_url, url)

        try:
            response = self.session.request(method, full_url, **kwargs)
            response.raise_for_status()  # 检查HTTP状态码
            return response
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")
            return None
        finally:
            # 遵守爬虫礼仪，添加延迟
            time.sleep(self.delay + random.uniform(0, 0.5))

    def crawl_page(self, url, parser=None):
        """爬取单个页面"""
        response = self.make_request(url)
        if response and response.status_code == 200:
            if parser:
                return parser(response.text)
            return response.text
        return None


# 高级爬虫类
class AdvancedCrawler(BasicCrawler):
    def __init__(self, base_url, use_selenium=False):
        super().__init__(base_url)
        self.use_selenium = use_selenium
        if use_selenium:
            self.anti_crawler = AntiAntiCrawler()
            self.anti_crawler.setup_selenium()

    def crawl_dynamic_content(self, url, wait_for=None):
        """爬取动态加载内容"""
        if not self.use_selenium:
            return self.crawl_page(url)

        self.anti_crawler.driver.get(urljoin(self.base_url, url))

        if wait_for:
            element = self.anti_crawler.smart_wait(By.CSS_SELECTOR, wait_for)
            if element:
                return self.anti_crawler.driver.page_source

        return self.anti_crawler.driver.page_source


class AntiAntiCrawler:
    def __init__(self):
        self.ua = UserAgent()
        self.driver = None

    def setup_selenium(self, headless=True):
        """配置Selenium浏览器驱动"""
        print(headless)
        options = webdriver.ChromeOptions()
        service = Service(executable_path="/Users/kj/Scripts/chromedriver")
        if headless:
            options.add_argument('--headless')
        # /Users/kj/Scripts/chromedriver
        # 反检测配置
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        self.driver = webdriver.Chrome(options=options, service=service)
        # 执行反检测脚本
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    def rotate_user_agent(self):
        """轮换User-Agent"""
        return self.ua.random

    def simulate_human_behavior(self, element):
        """模拟人类操作行为"""
        # 随机延迟
        time.sleep(random.uniform(1, 3))

        # 模拟鼠标移动
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(element).perform()
        time.sleep(random.uniform(0.5, 1.5))

        # 点击元素
        element.click()

    def handle_captcha(self, captcha_element):
        """处理验证码（基础版本）"""
        # 在实际项目中，这里可以集成第三方验证码识别服务
        print("检测到验证码，需要人工干预")
        input("请手动解决验证码后按回车继续...")

    def smart_wait(self, by, value, timeout=10):
        """智能等待元素加载"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except:
            print(f"元素加载超时: {by}={value}")
            return None


# # 使用示例
# crawler = BasicCrawler('http://m.smzdm.com')
# content = crawler.crawl_page('/youhui/')
# print(content)

# https://m.smzdm.com/p/164712502/
# 使用示例
crawler = AdvancedCrawler('http://m.smzdm.com', use_selenium=True)
content = crawler.crawl_dynamic_content('/youhui/')
details = parser.extract_smzdm_deals(content)
print(details)
