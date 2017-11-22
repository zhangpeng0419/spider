# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from spider.items import Images


class QidianSpider(scrapy.Spider):
	name = 'qidian'
	allowed_domains = ['qidian.com']
	start_urls = ['http://www.ivsky.com/bizhi/fengjing/']
	custom_settings = {
		'IMAGES_STORE':'downloadImage/',
		'IMAGES_EXPIRES':'90',
		'IMAGES_MIN_HEIGHT':110,
		'IMAGES_MIN_WIDTH':110,
		'IMAGES_THUMBS':{'small': (50, 50),'big': (270, 270),},
		'DOWNLOAD_DELAY':0.5,
    	'ITEM_PIPELINES':{'spider.downloadimagespipeline.DownLoadImagesPipeline': 300},
		'DOWNLOADER_MIDDLEWARES':{'spider.middlewares.ImagesFangDao': 543,},

	}



	def parse(self, response):
		imgs = response.xpath("//div[@class='left']//img/@src").extract()
		for img_url in list(set(imgs)):
			item = Images()
			item['images_urls'] = [img_url]
			yield item
