# spider
scrapy demo
本分支为简单的Scrapy利用spider简单爬取起点的数据
表结构如下
CREATE TABLE `qidian` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(55) DEFAULT NULL,
  `url` varchar(225) DEFAULT NULL,
  `author` varchar(45) DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  `wordcounts` varchar(45) DEFAULT NULL,
  `images_url` varchar(512) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1681 DEFAULT CHARSET=utf8