# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HamrobazaarItem(scrapy.Item):
    # define the fields for your item here like:
    phone = scrapy.Field()
    email = scrapy.Field()
    #address = scrapy.Field()
