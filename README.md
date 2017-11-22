# spider
scrapy demo

图片下载一般主要问题分为以下几点：
	1、常量的设置
		'IMAGES_STORE':'downloadImage/',
		'IMAGES_EXPIRES':'90',
		'IMAGES_MIN_HEIGHT':110,
		'IMAGES_MIN_WIDTH':110,
		'IMAGES_THUMBS':{'small': (50, 50),'big': (270, 270),},
	2、下载图片遇到防盗链接
		解决办法一： DEFAULT_REQUEST_HEADERS 中的referer为none
		解决办法二： 通过新建中间件添加referer为none
			class ImagesFangDao(object):
			    def process_request(self, request, spider):
			        referer = request.meta.get('referer', None)
			        if referer:
			            request.headers['referer'] = referer

