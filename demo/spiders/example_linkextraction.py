# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule

class ExampleLinkextractionSpider(CrawlSpider):
    name = 'example_linkextraction'
    allowed_domains = ["www.bacsiviet.vn"]
    start_urls = ['http://www.bacsiviet.vn/thuoc']
    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('span.step-links a[rel="next"]',)), callback='parse', follow=True),
    )
    def parse(self, response):
        print("parse")
