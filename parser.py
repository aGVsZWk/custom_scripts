# -*- coding: utf-8 -*-
# @Author  : HeLei
# @Time    : 2025/12/12 16:36
# @File    : data_parser.py
from bs4 import BeautifulSoup
import json
from typing import List, Dict
import re


class DataParser:
    @staticmethod
    def parse_with_bs4(html_content, selector):
        """使用BeautifulSoup解析HTML"""
        soup = BeautifulSoup(html_content, 'html.parser')
        elements = soup.select(selector)
        return [elem.get_text(strip=True) for elem in elements]

    @staticmethod
    def parse_with_regex(text, pattern):
        """使用正则表达式提取数据"""
        matches = re.findall(pattern, text)
        return matches

    @staticmethod
    def parse_json_data(json_text, key_path):
        """解析JSON格式数据"""
        try:
            data = json.loads(json_text)
            # 支持嵌套键路径解析
            keys = key_path.split('.')
            result = data
            for key in keys:
                result = result[key]
            return result
        except (json.JSONDecodeError, KeyError) as e:
            print(f"JSON解析错误: {e}")
            return None


# 综合解析示例
def comprehensive_parser(html_content):
    """综合多种解析方法的示例"""
    # 1. 使用BeautifulSoup提取结构化数据
    soup = BeautifulSoup(html_content, 'html.parser')
    title = soup.find('title').get_text() if soup.find('title') else ''

    # 2. 使用CSS选择器提取特定元素
    articles = soup.select('article.post')
    article_data = []

    for article in articles:
        data = {
            'title': article.select_one('h2').get_text(strip=True) if article.select_one('h2') else '',
            'content': article.select_one('.content').get_text(strip=True) if article.select_one('.content') else '',
            'date': article.select_one('.date').get_text(strip=True) if article.select_one('.date') else ''
        }
        article_data.append(data)

    # 3. 使用正则表达式提取特定模式
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', html_content)

    return {
        'page_title': title,
        'articles': article_data,
        'emails': emails
    }



# 假设你的HTML内容已经保存到变量 html_content 中
# html_content = open('aaa.html', 'r', encoding='utf-8').read()   # 如果是文件
# 这里直接使用你提供的文档内容（作为字符串）

def extract_smzdm_deals(html_content: str) -> List[Dict]:
    soup = BeautifulSoup(html_content, 'html.parser')

    # 找到所有商品卡片
    card_list = soup.find_all('li', class_='card-group-list')

    deals = []

    for card in card_list:
        deal = {}

        # 1. 详情页链接（相对路径转完整路径）
        a_tag = card.find('a')
        if a_tag and 'href' in a_tag.attrs:
            relative_href = a_tag['href']  # 如 /p/164680594/
            deal['link'] = 'https://m.smzdm.com' + relative_href.rstrip('/') + '/'

        # 2. 商品标题（可能包含 button 标签，如“国民爆款”）
        title_div = card.find('div', class_='card-title')
        if title_div:
            # 去除 button 标签内容，只保留纯标题文本
            # 先复制一份，删除 button，然后取文本
            title_copy = title_div.__copy__()
            for btn in title_copy.find_all('button'):
                btn.decompose()
            deal['title'] = title_copy.get_text(strip=True)

        # 3. 价格
        price_div = card.find('div', class_='card-price')
        if price_div:
            deal['price'] = price_div.get_text(strip=True)

        # 4. 商城和发布时间
        actions_left = card.find('div', class_='card-actions-left')
        if actions_left:
            spans = actions_left.find_all('span')
            if len(spans) >= 1:
                mall_span = spans[0].find('span', class_='card-mall')
                if mall_span:
                    deal['mall'] = mall_span.get_text(strip=True)
                # 发布时间在同一个 span 的第二个子 span
                time_span = spans[0].find_all('span')[1] if len(spans[0].find_all('span')) > 1 else None
                if time_span:
                    deal['time'] = time_span.get_text(strip=True)

        # 只保留有关键信息的项
        if deal.get('title') and deal.get('price') and deal.get('link'):
            deals.append(deal)
    return deals

# 使用示例
# html_content = """<你的完整HTML内容>"""
# deals = extract_smzdm_deals(html_content)

# 打印结果（格式化字典列表）
# for i, deal in enumerate(deals, 1):
#     print(f"{i}. {deal}")

# 返回示例（部分）：
# [
#     {'title': '剑南春 水晶剑 52%vol 白酒 750mL 单瓶装', 'price': '479元', 'mall': '京东', 'time': '12-16', 'link': 'https://post.smzdm.com/p/164680594/'},
#     {'title': '骆驼 男士弹力直筒休闲牛仔裤', 'price': '132.05元（需用券）', 'mall': '天猫精选', 'time': '19:09', 'link': 'https://post.smzdm.com/p/164735719/'},
#     ...
# ]