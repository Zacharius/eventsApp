import os
import scrapy
from scrapy import Request
import mysql.connector
from mysql.connector import Error

class QuotesSpider(scrapy.Spider):
    name = "events"

    def start_requests(self):
        urls = [
            'http://tpr.org/community-calendar',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
       for event in response.css('li.event-stub'):
           relative_url = response.css('div.row.padding-medium div.column.small-12.medium-10 h2 a::attr("href")').extract_first()
           absolute_url = response.urljoin(relative_url)
           date = event.css('div.short-date::text').extract_first(),
           title = event.css('a::text').extract_first(),
           venue = event.css('li.icon.venue::text').extract_first(),
           yield Request(absolute_url, callback=self.parse_page, meta={'date': date, 'title': title, 'venue': venue})
       
       relative_next_url = response.xpath('//a[@title="Go to next page"]/@href').extract_first()
       absolute_next_url = response.urljoin(relative_next_url)
       yield scrapy.Request(absolute_next_url, callback = self.parse)

    def parse_page(self, response):
        date = response.meta.get('date')
        title = response.meta.get('title')
        venue = response.meta.get('venue')
        des = response.css('div.content div.row.collapse.description p::text').extract()
        address = response.css('ul.event-venue li::text').extract()
        addr = address[0];
        cost = response.css('li.icon.price::text').extract()
        if cost is 'null':
            cost = 0
        time = response.css('li.icon.time::text').extract()
        cats = response.css('li.categories a::text').extract()
        dow = response.css('div.dayofweek::text').extract()
        


        yield {
               'date': date,
               'title': title,
               'venue': venue,
               'des': des,
               'address' : addr,
                'cost' : cost,
                'time' : time,
                'cats' : cats,
                'dow' : dow

               }




        
