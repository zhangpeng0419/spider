# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from spider.items import QiDian


class QidianSpider(CrawlSpider):
	name = 'qidian'
	allowed_domains = ['qidian.com']
	start_urls = ['https://www.qidian.com/all']
	custom_settings = {
		'DOWNLOAD_DELAY':0.5,
		'ITEM_PIPELINES':{'spider.pipelines.ToSpiderQiDian': 300},
		'DEFAULT_REQUEST_HEADERS':{'accept': 'image/webp,*/*;q=0.8','accept-language': 'zh-CN,zh;q=0.8','referer': 'https://www.qidian.com','user-agent': 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36',}
	}
	rules = (
		Rule(LinkExtractor(allow=('https://book.qidian.com/info/\d+', )), callback='parse_item'),
    )


	def parse_item(self, response):
		item = QiDian()
		item['name'] = response.xpath("//div[contains(@class,'book-information')]//h1/em/text()").extract()[0]

		item['url'] = response.url

		item['author'] =  response.xpath("//div[contains(@class,'book-information')]//a[@class='writer']/text()").extract()[0]

		item['status'] =  response.xpath("//div[contains(@class,'book-information')]//span[@class='blue']/text()").extract_first()

		item['wordcounts'] = ''

		item['images_url'] =  response.xpath("//div[contains(@class,'book-information')]/div[@class='book-img']//img/@src").extract_first()

		yield item
