# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ClaimLine(Item):
    type = Field()
    url = Field()
    claim_id = Field()
    claim_value = Field()
    date = Field()
    description = Field()
    category = Field()
    subcategory = Field()
    value = Field()
    status = Field()


class ReceiptLine(Item):
    type = Field()
    file_urls = Field()
    files = Field()
    claim_id = Field()
    name = Field()
