# -*- coding: utf-8 -*-
import scrapy
from spider.items import ToRedis

class ParseUrlSpider(scrapy.Spider):
    name = 'parseurl'
    allowed_domains = ['vsky.com']
    start_urls = ['http://www.ivsky.com/tupian/ziranfengguang/']
    custom_settings = {
        'ITEM_PIPELINES':{'spider.pipelines.ToRedis': 300},
        }

    def parse(self, response):
		# print(response.body)
		list = response.xpath("//ul[@class='ali']//img/@src").extract()
		for img in list:
			item = ToRedis()
			item['images_urls'] = img
			yield item


