# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request
from scrapy.http import FormRequest

class GitHubeSpider(Spider):
    name = 'githubbycookie'
    img_urls = []
    allowed_domains = ['github.com']

    custom_settings = {
        'DOWNLOAD_DELAY':0.5,
        'DEFAULT_REQUEST_HEADERS':{'accept': 'image/webp,*/*;q=0.8','accept-language': 'zh-CN,zh;q=0.8','referer': 'http://www.docker.org.cn','user-agent': 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36',}
        }
    cookies={
		'_octo':'GH1.1.692643607.1511181470',
		'logged_in':'yes',
		'dotcom_user':'zhangpeng0419',
		'user_session':'-oeB_haaEeQivEzsctAATLdUx7_4v41XRgAebRE7sJs9KW05',
		'__Host-user_session_same_site':'-oeB_haaEeQivEzsctAATLdUx7_4v41XRgAebRE7sJs9KW05',
		'_gh_sess':'eyJsYXN0X3dyaXRlIjoxNTExMzMzMjY2NDQzLCJmbGFzaCI6eyJkaXNjYXJkIjpbImFuYWx5dGljc19kaW1lbnNpb24iLCJhbmFseXRpY3NfbG9jYXRpb24iXSwiZmxhc2hlcyI6eyJhbmFseXRpY3NfZGltZW5zaW9uIjp7Im5hbWUiOiJkaW1lbnNpb241IiwidmFsdWUiOiJMb2dnZWQgSW4ifSwiYW5hbHl0aWNzX2xvY2F0aW9uIjoiL2Rhc2hib2FyZCJ9fSwic2Vzc2lvbl9pZCI6Ijc2NzQ5OTIyNDVjOWM1MGYwMzRkZDYxZmQ0YzIxOThmIiwibGFzdF9yZWFkX2Zyb21fcmVwbGljYXMiOjE1MTEzMzMyNjgyMjAsImNvbnRleHQiOiIvIn0%3D--69212a1679ad887e3f18e5687a77bd94fbbcc935',
		'_ga':'GA1.2.1563700060.1511181470',
		'_gat':'1',
		'tz':'Asia%2FShanghai',
    }

    def start_requests(self):
		return [scrapy.Request(url='https://github.com',cookies=self.cookies,callback=self.login,dont_filter=True,)]

    def login(self, response):
		print(response.body)


