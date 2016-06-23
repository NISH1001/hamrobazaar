from scrapy.spiders import BaseSpider
from scrapy.selector import Selector
from scrapy.http import Request

from hamrobazaar.items import HamrobazaarItem

class HamroSpider(BaseSpider):
    name = "hamrospider"
    allowed_domains = ["hamrobazaar.com"]
    start_urls = [
            "http://hamrobazaar.com/c3-computer-and-peripherals",
        ]

    def parse(self, response):
        sel = Selector(response)
        item = HamrobazaarItem()
        item['phone'] = "123"
        yield item

