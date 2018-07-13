  
# -*- coding: utf8 -*-
import scrapy
import httplib2
import json
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import datetime
class SohoaVnexpressNet(CrawlSpider):
    name = "crawlervn"
    allowed_domains = ["genk.vn"]
    start_urls = ['http://genk.vn/']

    # rules = (
    #     Rule(LinkExtractor(allow=('http://genk\.vn')), callback='parse_item', follow=False),
    # )

    start_urls = ['http://genk.vn/']
    def start_requests(self):
        urls = []
        for x in range(1,11):
            url = "http://genk.vn/ajax-home/page-" + str(x) + "/_.chn"
            urls.append(url)

        for url in urls :
            yield scrapy.Request(url=url, callback=self.parse_artilce)
        print("ters");


    def parse_artilce(self, response):
        domainUrl = "http://genk.vn"
        xpathATags = response.xpath('//li');
        data = []
        for i in xpathATags :
            artilce = {}
            xpathLeft = i.xpath('.//div[@class="knswli-left fl"]//a');
            xpathRight = i.xpath('.//div[@class="knswli-right elp-list"]')
            artilce['title'] =  xpathLeft.xpath('./@title').extract()[0];
            artilce['image'] = xpathLeft.xpath('./img/@src').extract()[0];
            artilce['sourceUrl'] = domainUrl  + xpathLeft.xpath('./@href').extract()[0];
            artilce['subContent'] = xpathRight.xpath('.//span[@class="knswli-sapo"]/node()').extract()[0];
            artilce['sourcePage'] = 'Genk';
            artilce['typeOrHumanSource'] = xpathRight.xpath('.//a[@class="knswli-category"]/@title').extract()[0];
            data.append(artilce);
            print("Test");
        print("artical");
        http = httplib2.Http()
        content = http.request("http://192.168.1.143:1310/parse/functions/saveNewsItem",
                        method="POST",
                        headers={'Content-type': 'application/json', 'X-Parse-Application-Id' : 'pnews-app-id' },
                        body = json.JSONEncoder().encode({"data": data}) )

        return data
