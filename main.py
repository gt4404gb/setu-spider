from scrapy import cmdline
import logging
logging.getLogger('scrapy').setLevel(logging.ERROR)

cmdline.execute('scrapy crawl setu'.split())
'''
import scrapy
from scrapy.crawler import CrawlerProcess
from setu.spiders.setu import SetuSpider

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(SetuSpider)
    process.start()
'''