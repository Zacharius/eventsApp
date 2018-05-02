import scrapy

class theCurrentEventsSpider(scrapy.Spider):
    name= "theCurrent"

    start_urls = [
        "https://www.sacurrent.com/sanantonio/EventSearch"
    ]

    def parse(self, response):

        eventPages = response.css('div.listing > h3 > a::attr(href)').extract()

        for eventPage in eventPages :
            yield scrapy.Request(eventPage, callback=self.parseEvent)
                                     

    def parseEvent(self, response):

        title = response.css('h1.listingTitle::text')[1].extract().strip()

        dateText = response.css('span.eventWhen::text').extract_first().strip()

        date = response.css('span.eventWhen::text').re(r'\w+ \d+')[0]

        priceText = response.css('span.eventPrice::text').extract_first().strip()

        if priceText == 'Free':
            price = 0
        else:
            price = response.css('span.eventPrice::text').re(r'\d+')[0]

        desc = response.css('div.descr_txt::text').extract_first().strip()

        sourceLink = response.css('span.eventUrl a::attr(href)').extract_first()

        imgLoc = response.css('link["rel=image_src"]::atr(href)').extract_first()
        

        yield {
            'title' : title,
            'dateText' : dateText,
            'date' : date,
            'priceText' : priceText,
            'price' : price,
            'desc' : desc,
            'sourceLink' : sourceLink,
            'imgLoc' : imgLoc,
        }



            
                         
            
                         
