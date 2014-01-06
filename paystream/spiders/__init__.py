# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from scrapy.spider import BaseSpider
from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import FormRequest, Request
from scrapy.selector import Selector
from scrapy import log
from scrapy.utils.project import get_project_settings

from paystream.items import ClaimLine, ReceiptLine
from IPython import embed



class LoginSpider(BaseSpider):
    name = 'paystream'
    start_urls = ['https://portal.paystream.co.uk/']

    def parse(self, response):
        settings = get_project_settings()
        return [FormRequest.from_response(response,
                    formdata={'username': settings['USERNAME'], 'password': settings['PASSWORD']},
                    callback=self.after_login)]

    def after_login(self, response):
        settings = get_project_settings()
        # check login succeed before going on
        if "authentication failed" in response.body:
            self.log("Login failed", level=log.ERROR)
            return
        else:
            self.log("I'm in")

        for num in range(settings['LAST'] + 1):
            yield Request("https://portal.paystream.co.uk/Expenses/Receipted/View/{}".format(num), callback=self.parse_claim)

    def parse_claim(self, response):
        sel = Selector(response)
        receipted_expense_claim = sel.xpath("//h2[contains(text(),'Receipted Expense Claim')]/text()")[0].extract().strip().split("\n")
        claim_id = receipted_expense_claim[1].strip()
        claim_value = receipted_expense_claim[2].strip().split(" ")[-1].replace(u'\u00A3', '').strip()
#        embed()
        lines = sel.xpath("//table/tbody/tr[td]")
        items = []
        for line in lines:
            values = map(lambda x: x.strip().replace(u'\u00A3', ''), line.xpath("td/text()").extract())
            item = ClaimLine()
            item['type'] = 'expense'
            item['claim_id'] = claim_id
            item['claim_value'] = claim_value
            item['url'] = response.url
            item['date'] = values[0]
            item['description'] = values[1]
            item['category'] = values[2]
            item['subcategory'] = values[3]
            item['value'] = values[4]
            item['status'] = values[6]
            items.append(item)

        downloadables = sel.xpath("//ul/li/a[contains(@href, 'DownloadReceipt')]")
        for downloadable in downloadables:
            receipt = ReceiptLine()
            receipt['type'] = 'receipt'
            receipt['file_urls'] = ["https://portal.paystream.co.uk{}".format(downloadable.xpath('@href').extract()[0])]
            receipt['name'] = downloadable.xpath('text()').extract()
            receipt['claim_id'] = claim_id
            items.append(receipt)

        return items
