from scrapy_redis.spiders import RedisSpider
from spider.items import Files


class Spider(RedisSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'download'
    redis_key = 'downloadurl'
    custom_settings = {
            'ITEM_PIPELINES':{'spider.pipelines.DownLoadFilesPipeline': 300},
            }

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(Spider, self).__init__(*args, **kwargs)

    def parse(self, response):
        item = Files()
        item['file_urls'] = response.url
        yield item