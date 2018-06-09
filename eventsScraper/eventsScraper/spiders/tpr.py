import os
import scrapy
from scrapy import Request

class QuotesSpider(scrapy.Spider):
    name = "tpr"

    start_urls = [
            'http://tpr.org/community-calendar'
        ]

    def parse(self, response):
       for event in response.css('li.event-stub'):
           relative_url = response.css('div.row.padding-medium div.column.small-12.medium-10 h2 a::attr("href")').extract_first()
           absolute_url = response.urljoin(relative_url)
           date = event.css('div.short-date::text').extract_first().strip(),
           title = event.css('a::text').extract_first(),
           venue = event.css('li.icon.venue::text').extract_first().strip(),
           yield Request(absolute_url, callback=self.parse_page, meta={'date': date, 'title': title, 'venue': venue})
       
       relative_next_url = response.xpath('//a[@title="Go to next page"]/@href').extract_first()
       absolute_next_url = response.urljoin(relative_next_url)
       yield scrapy.Request(absolute_next_url, callback = self.parse)

    def parse_page(self, response):
        dateText = response.css("li.date-summary::text").extract_first().strip()
        date = response.css("li.date-summary::text").re(r"\w+\.* \d+")[0]
        title = response.css("h1.title::text").extract_first()
        address = "\n".join(response.css("ul.event-venue li::text").extract())
        desc = response.css('div.content div.row.collapse.description p::text').extract_first()
        venue = response.css('li.icon.venue::text').extract_first()
        priceText = response.css('li.icon.price::text').extract_first()
        if not priceText or priceText == 'Free':
            price = 0
        else:
            price = response.css('li.icon.price::text').re(r'\d+')[0]
        category = response.css('li.categories a::text').extract_first()
        if not category:
            category = ""
        imgLoc = response.css('div.event-image img::attr(src)').extract_first()
        if not imgLoc:
            imgLoc = ""
        sourceLink = response.url
        



        yield {
                'title' : title,
                'dateText' : dateText,
                'date' : date,
                'priceText' : priceText,
                'price' : price,
                'desc' : desc,
                'sourceLink' : sourceLink,
                'imgLoc' : imgLoc,
                'sourceLink' : sourceLink,
                'category' : category,
                'venue' : venue
            }




        
