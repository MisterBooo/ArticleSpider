# -*- coding: utf-8 -*-
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/110287/']

    def parse(self, response):
        # // *[ @ id = "post-110287"] / div[1] / h1
        response_selector = response.xpath("/html/body/div[3]/div[3]/div[1]/div[1]/h1")
        pass
