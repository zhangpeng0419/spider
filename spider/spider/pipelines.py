# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector
import sys
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

