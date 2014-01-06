# Scrapy settings for paystream project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import os

ROOT = os.path.dirname(os.path.realpath(__file__))


BOT_NAME = 'paystream'

SPIDER_MODULES = ['paystream.spiders']
NEWSPIDER_MODULE = 'paystream.spiders'

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.73.11 (KHTML, like Gecko) Version/7.0.1 Safari/537.73.11'

ITEM_PIPELINES = {
    'paystream.pipelines.files.FilesPipeline': 100,
}

FILES_STORE = os.path.join(ROOT, 'downloads')


USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']
LAST = int(os.environ['LAST'])
