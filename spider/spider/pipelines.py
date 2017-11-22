# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector
import sys
import redis
import scrapy
from scrapy.pipelines.files import FilesPipeline
from scrapy.exceptions import DropItem
reload(sys)
sys.setdefaultencoding('utf-8')


def dbHandle():
	conn = mysql.connector.connect(
		host = "111.231.197.82",
		user = "root",
		passwd = "rentianqi123456",
		charset = "utf8",
		use_unicode = False
	)
	return conn

class SpiderPipeline(object):
    def process_item(self, item, spider):
        return item

class ToSpiderQiDian(object):
	"""docstring for QiDian"""
	def process_item(self,item,spider):
		dbObject = dbHandle()
		cursor = dbObject.cursor()
		cursor.execute("USE spider")
		sql = "INSERT INTO qidian(`name`,`url`,`author`,`status`,`wordcounts`,`images_url`) VALUES(%s,%s,%s,%s,%s,%s)"
		try:
			cursor.execute(sql,(item['name'],item['url'],item['author'],item['status'],item['wordcounts'],item['images_url']))
			dbObject.commit()
		except BaseException as e:
			print("error>>>>>>>>>>>>>",e,"<<<<<<<<<<<<<error")
			dbObject.rollback()
		return item

class ToRedis(object):
	"""docstring for QiDian"""
	def process_item(self,item,spider):
		try:
			r = redis.Redis(host='111.231.197.82', port=6379, db=0,password='rentianqi123456')
			r.lpush('downloadurl',item['images_urls'])
		except BaseException as e:
			print("error>>>>>>>>>>>>>",e,"<<<<<<<<<<<<<error")
		return item

class DownLoadFilesPipeline(FilesPipeline):

	def get_media_requests(self, item, info):
		yield scrapy.Request(item["file_urls"])

	def item_completed(self, results, item, info):
		file_paths = [x["path"] for ok, x in results if ok]
		if not file_paths:
			raise DropItem("Item contains no files")
		item['file_paths'] = file_paths
		return item