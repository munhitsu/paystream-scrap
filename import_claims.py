from scrapy.item import Item, Field
from scrapy.contrib.spiders import CrawlSpider
from scrapy.spider import BaseSpider


class ClaimLine(Item):
    week = Field()
    description = Field()
    category = Field()
    subcategory = Field()
    value = Field()
    status = Field()



class ReceiptLine(Item):
    uploaded = Field()





class PaystreamSpider(CrawlSpider):
    name = 'paystream'
    allowed_domains = 'portal.paystream.co.uk'
    start_urls = ['']
#    rule =

#    def parse
