# -*- coding: utf-8 -*-
import scrapy

from scrapy_master.items import ScrapyMasterItem


class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['moive.douban.com']
    start_urls = ['https://movie.douban.com/chart']

    def parse(self, response):
        move_list = response.xpath("//div[@class='article']//div[@class='indent']//table[@width='100%']")
        for item in move_list:
            douban_item = ScrapyMasterItem()
            douban_item['movive_name'] = item.xpath("normalize-space(.//div[@class='pl2']//a/text())").extract_first()
            douban_item['introduce'] = item.xpath(".//div[@class='pl2']//p[@class='pl']/text()").extract_first()
            douban_item['star'] = item.xpath(".//div[@class='star clearfix']//span[@class='rating_nums']/text()").extract_first()
            douban_item['evaluate'] = item.xpath(".//div[@class='star clearfix']//span[@class='pl']/text()").extract_first()
            print(douban_item)
        #pass