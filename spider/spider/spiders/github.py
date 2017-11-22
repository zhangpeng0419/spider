# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.http import FormRequest

class GitHubSpider(scrapy.Spider):
	name = 'github'
	allowed_domains = ['github.com']
	start_urls = ['https://github.com/login']
	custom_settings = {
        'COOKIES_ENABLES':True,
        'DOWNLOAD_DELAY':0.5,
        }
	post_headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36",
        "Referer": "https://github.com/",
    }

	def start_requests(self):
		return [scrapy.Request(url='https://github.com/login',meta={'cookiejar': 1},callback=self.login,dont_filter=True,)]

	def login(self, response):
		authenticity_token = response.xpath("//input[@name='authenticity_token']/@value").extract()[0]
		form={
	        'commit':'Sign in',
	        'utf8':'✓',
	        'authenticity_token':authenticity_token,
	        'login':'496990965@qq.com',
	        'password':'*************',
	    }
		return [ FormRequest(
	                'https://github.com/session',
	                meta={'cookiejar': response.meta['cookiejar']},
	                callback=self.after_login,
	                formdata=form,
	                headers=self.post_headers,
	                dont_filter=True) ]

	def after_login(self, response):
		print(response.body)
