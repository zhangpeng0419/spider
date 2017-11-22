import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

class DownLoadImagesPipeline(ImagesPipeline):

	def get_media_requests(self, item, info):
		for url in item["images_urls"]:
			yield scrapy.Request(url)

	def item_completed(self, results, item, info):
		image_path = [x["path"] for ok, x in results if ok]
		if not image_path:
			raise DropItem("Item contains no images")
		item['image_paths'] = image_path
		return item