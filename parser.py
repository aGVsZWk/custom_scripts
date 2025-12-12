# -*- coding: utf-8 -*-
# @Author  : HeLei
# @Time    : 2025/12/12 16:36
# @File    : data_parser.py
from bs4 import BeautifulSoup
import re
import json


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
