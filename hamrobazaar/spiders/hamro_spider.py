from scrapy.spiders import BaseSpider
from scrapy.selector import Selector
from scrapy.http import Request

from hamrobazaar.items import HamrobazaarItem

class HamroSpider(BaseSpider):
    name = "hamrospider"
    allowed_domains = ["hamrobazaar.com"]
    start_urls = [
            "http://hamrobazaar.com/c1-automobiles",
            "http://hamrobazaar.com/c2-mobile-and-accessories",
            "http://hamrobazaar.com/c260-business-and-industrial",
            "http://hamrobazaar.com/c3-computer-and-peripherals",
            "http://hamrobazaar.com/c4-consumer-electronics",
            "http://hamrobazaar.com/c5-toys-and-video-games",
            "http://hamrobazaar.com/c6-apparels-and-accessories",
            "http://hamrobazaar.com/c7-home-furnishing-and-appliances",
            "http://hamrobazaar.com/c8-music-and-sports",
            "http://hamrobazaar.com/c9-beauty-and-health",
            "http://hamrobazaar.com/c10-books-and-learning",
        ]

    # parse the items in the category
    def parse(self, response):
        selec = Selector(response)

        selectors = response.xpath("/html/body/table/tr[2]/td/table/tr[1]/td/table[5]/tr/td[2]//table")
        for sel in selectors:
            link = sel.xpath("./tr[1]/td[3]/a[1]/@href").extract_first()
            if link:
                full_link = response.urljoin(link)
                yield Request(full_link, callback=self.parse_detail, meta={"url" : full_link})

                next_url = response.urljoin(response.xpath("//a[contains(.//text(), \'Next\')]/@href").extract_first())
                yield Request(next_url, callback=self.parse)

    # parse the details
    def parse_detail(self, response):
        selec = Selector(response)
        item = HamrobazaarItem()
        phone = response.xpath("//td[@id='white']/text()").re(r"9[0-9]{9}")
        phone = list(set(phone))
        if phone:
            item['phone'] = phone
        yield item


