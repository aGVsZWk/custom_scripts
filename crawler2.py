# -*- coding: utf-8 -*-
# @Author  : HeLei
# @Time    : 2025/12/12 16:47
# @File    : crawler2.py
import asyncio
import aiohttp
from concurrent.futures import ThreadPoolExecutor
import redis
import hashlib


class OptimizedCrawler:
    def __init__(self, max_concurrent=10):
        self.max_concurrent = max_concurrent
        self.redis_client = redis.Redis(host='localhost', port=6379, db=0)

    async def async_crawl(self, urls):
        """异步并发爬取"""
        connector = aiohttp.TCPConnector(limit=self.max_concurrent)
        timeout = aiohttp.ClientTimeout(total=30)

        async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
            tasks = [self.fetch_url(session, url) for url in urls]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            return results

    async def fetch_url(self, session, url):
        """异步获取单个URL"""
        try:
            async with session.get(url) as response:
                content = await response.text()

                # 内容去重
                content_hash = hashlib.md5(content.encode()).hexdigest()
                if not self.is_duplicate(content_hash):
                    return content
                return None
        except Exception as e:
            print(f"异步爬取失败 {url}: {e}")
            return None

    def is_duplicate(self, content_hash):
        """基于Redis的内容去重"""
        key = f"content:{content_hash}"
        if self.redis_client.exists(key):
            return True
        self.redis_client.setex(key, 86400, 1)  # 24小时缓存
        return False

    def batch_process(self, data_list, processor, batch_size=100):
        """批量数据处理"""
        with ThreadPoolExecutor(max_workers=4) as executor:
            batches = [data_list[i:i + batch_size] for i in range(0, len(data_list), batch_size)]
            results = list(executor.map(processor, batches))
            return [item for sublist in results for item in sublist]


# 性能优化示例
async def main():
    urls = [f"https://example.com/page{i}" for i in range(1, 101)]
    crawler = OptimizedCrawler(max_concurrent=20)

    results = await crawler.async_crawl(urls)
    valid_results = [r for r in results if r is not None]

    print(f"成功爬取 {len(valid_results)} 个页面，去重后 {len(valid_results)} 个唯一内容")

# 运行异步爬虫
# asyncio.run(main())
