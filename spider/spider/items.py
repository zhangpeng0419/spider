# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join



class SpiderItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass



class QiDian(Item):
	"""docstring for QiDian"""
	name = Field()
	url = Field()
	author = Field()
	status = Field()
	wordcounts = Field()
	images_url = Field()

class Files(Item):
	file_urls = Field()
	file_paths = Field()
