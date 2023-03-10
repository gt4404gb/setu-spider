# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
from ..items import SetuItem #..代表上一级
from scrapy_splash import SplashRequest

class SetuSpider(CrawlSpider):
    #定义爬虫名
    name = "setu"
     #搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页
    allowed_domains = ["m4ex.com","m4ex.net"]
    #开始页面
    start_urls = ['http://m4ex.com/fantasy/devil']
    #print(start_urls)

    # 设置爬虫的请求头，防止爬取失败
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
    }

    rules = (
        # 提取匹配 allow正则匹配的链接，并使用spider的parse2方法进行分析
        Rule(LinkExtractor(allow=('/.*?/[a-z]+.*?[0-9]+', )), callback='parse2',follow=True),
    )

    def parse2(self, response):
        #proxy = "http://127.0.0.1:1087"
        item = SetuItem()
        item['image_urls'] = response.xpath('//img[@class="aligncenter size-full"]/parent::a[contains(@href, "m4ex.net")]/@href').extract()
        item['num'] = response.xpath('//div[@class="num"]//text()').extract()
        item['tag'] = response.xpath('//a[@rel="category tag"]//text()').extract_first()
        item['title'] = response.xpath('//h1[@class="entry-title"]//text()').extract_first()
        yield item
        print("返回item成功")
        #这里好像写错了，最后这个yield去掉应该也可以
        yield scrapy.Request(response.url, callback=self.parse)
