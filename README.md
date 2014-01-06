paystream.co.uk scrap
=====================

A quick quick hack to download your data that you've recorded in paystream.co.uk web app.
It downloads claimed expenses and also uploaded receipts.
Based on [scrapy](http://doc.scrapy.org) framework/library.

Example usage:

    USERNAME=email@example.com PASSWORD=foobar LAST=5 scrapy crawl paystream -o items.json -t json

 - USERNAME - your username
 - PASSWORD - your password
 - LAST is the number of claims you've made
 
Installation
---------------
required python (tested on 2.7):

    pip install -r requirements.txt
 