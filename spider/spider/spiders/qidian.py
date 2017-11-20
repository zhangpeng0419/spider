# -*- coding: utf-8 -*-
import scrapy
from spider.items import QiDian


class QidianSpider(scrapy.Spider):
	name = 'qidian'
	allowed_domains = ['qidian.com']
#start_urls = ['https://www.qidian.com/all']
	start_urls = ['https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=62']
	custom_settings = {
#'DOWNLOAD_DELAY':0.5,
    	'ITEM_PIPELINES':{'spider.pipelines.ToSpiderQiDian': 300},
    	'DEFAULT_REQUEST_HEADERS':{'accept': 'image/webp,*/*;q=0.8','accept-language': 'zh-CN,zh;q=0.8','referer': 'https://www.qidian.com','user-agent': 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36',}
	}

	def parse(self, response):
		lists = response.xpath("//ul[contains(@class,'all-img-list')]/li")
		for div in lists:
			item = QiDian()
			item['name'] = div.xpath("div[@class='book-mid-info']//h4/a/text()").extract()[0]
			item['url'] = div.xpath("div[@class='book-mid-info']//h4/a/@href").extract()[0]
			item['author'] = div.xpath("div[@class='book-mid-info']//p[@class='author']/a[@class='name']/text()").extract()[0]
			item['status'] = div.xpath("div[@class='book-mid-info']//p[@class='author']/span/text()").extract()[0]
			item['wordcounts'] = div.xpath("div[@class='book-mid-info']//p[@class='update']/span/text()").extract()[0]
			item['images_url'] = div.xpath("div[@class='book-img-box']//img/@src").extract()[0]
			yield item
		next_page = response.xpath("//ul[@class='lbf-pagination-item-list']/li[last()]/a/@href").extract()[0]
		if next_page:
			yield	scrapy.Request("http://"+next_page, callback=self.parse)
