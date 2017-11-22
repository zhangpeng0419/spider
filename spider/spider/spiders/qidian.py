# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from spider.items import Files


class QidianSpider(scrapy.Spider):
	name = 'qidian'
	allowed_domains = ['qidian.com']
	start_urls = ['https://www.qidian.com/all']

	custom_settings = {
		'FILES_STORE':'downloadfiles/',
		'FILES_EXPIRES':'90',
		'DOWNLOAD_DELAY':0.5,
    	'ITEM_PIPELINES':{'spider.downloadfilepipeline.DownLoadFilesPipeline': 300},
    	'DEFAULT_REQUEST_HEADERS':{'accept': 'image/webp,*/*;q=0.8','accept-language': 'zh-CN,zh;q=0.8','referer': 'https://www.qidian.com','user-agent': 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36',}
	}



	def parse(self, response):
		item = Files()
		item['file_urls'] = ['https://qidian.gtimg.com/qd/images/common/share.96a8f.png','https://book.qidian.com/ejs/qd/js/book_details/fansHall.d3908.ejs']#"http:"+response.xpath("//div[contains(@class,'book-information')]//img/@src").extract_first()
		yield item
