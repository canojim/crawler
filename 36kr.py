#!/usr/bin/python

import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    base_url = 'http://36kr.com/'
    start_urls = [base_url]

    #TODO: Warn if no link found
    def parse(self, response):
        #Fetch URL from main page
        for url in response.xpath("//a[@class=\"title info_flow_news_title\"]/@href").extract():
        	print "url: ", url
        	yield scrapy.Request(response.urljoin(url), self.parse_titles)
    	
    def parse_titles(self, response):
    	#Add Logic to handle article page
    	title = response.xpath("//h1[@class='single-post__title']/text()").extract()[0]
    	content = response.xpath("//section[@class='article']/p/text()").extract()[0]

        yield {'title': title, 'content': content}
