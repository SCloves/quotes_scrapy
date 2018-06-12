# -*- coding: utf-8 -*-
import scrapy


class AuthorsSpider(scrapy.Spider):
    name = 'authors'
    start_urls = ['http://quotes.toscrape.com/']
    
    def parse(self, response):
        # paginação
        next_url = response.css("li.next > a::attr(href)").extract_first()
        if next_url:
            next_page_url = response.urljoin(next_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
