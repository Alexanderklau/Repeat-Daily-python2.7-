from scrapy.selector import Selector
from scrapy import Spider
from wikispider.items import Article
from scrapy.contrib.linkextractors.sgml import *
from scrapy.contrib.spiders import CrawlSpider,Rule
r


class ArticleSpider(CrawlSpider):
    name = "article"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["http://en.wikipedia.org/wiki/Main_Page",
                  "heep://en.wikipedia.org/wiki/Python_%28programming_language%29"]
    rules = [Rule(SgmlLinkExtractor(allow=('(/wiki/)((?!:).)*$'),),
                  callback="parse_item",follow=True)]
    def parse_item(self, response):
        item = Article()
        title = response.xpath('//h1/text()')[0].extract()
        print("Title is:" +title)
        item['title'] = title
        return item

