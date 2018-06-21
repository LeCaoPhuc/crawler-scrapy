
# -*- coding: utf8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class SohoaVnexpressNet(CrawlSpider):
    name = "crawlervn"
    allowed_domains = ["genk.vn"]
    start_urls = ['http://genk.vn/']

    # rules = (
    #     Rule(LinkExtractor(allow=('http://genk\.vn')), callback='parse_item', follow=False),
    # )

    start_urls = ['http://genk.vn/']
    def start_requests(self):
        urls = [
            'http://genk.vn/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_artilce)


    def parse_artilce(self, response):
        data = []
        xpathATags = response.xpath('//div[@class="knswli-left fl"]//a');
        for i in xpathATags :
            artilce = {}
            artilce['title'] =  i.xpath('./@title').extract()[0];
            artilce['image'] = i.xpath('./img/@src').extract()[0];
            artilce['sourceUrl'] = response.url  + i.xpath('./@href').extract()[0];
            # data.append(artilce);
            return artilce
        print("Test");