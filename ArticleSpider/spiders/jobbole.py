# -*- coding: utf-8 -*-
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/110287/']

    def parse(self, response):
        # // *[ @ id = "post-110287"] / div[1] / h1
        re2_selector = response.xpath('//*[@id="post-110287"]/div[1]/h1/text()')
        re3_selector = response.xpath("/html/body/div[1]/div[3]/div[1]/div[1]/h1/text()")
        re_selector = response.xpath("/html/body/div[3]/div[3]/div[1]/div[1]/h1")
        # 推荐使用class型，因为后期循环爬取可扩展通用性强。
        re4_selector = response.xpath('//div[@class="entry-header"]/h1/text()')

        pass
