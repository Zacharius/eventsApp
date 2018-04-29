import scrapy

class theCurrentEventsSpider(scrapy.Spider):
    name= "theCurrent"

    start_urls = [
        "https://www.sacurrent.com/sanantonio/EventSearch"
    ]

    def parse(self, response):

        print('hello world!!!!!!')
        eventPages = response.css('div.listing > h3 > a::attr(href)').extract()

        for eventPage in eventPages :
            print(eventPage)
            yield scrapy.Request(eventPage, callback=self.parseEvent)
                                 
        

    def parseEvent(self, response):

        yield {
            'title' : 
                 response.css('h1.listingTitle::text')[1].extract().strip(),
            'dateText' :
                 response.css('span.eventWhen::text').extract_first().strip(),
            'priceText' :
                 response.css('span.eventPrice::text').extract_first().strip(),
            'desc' :
                 response.css('div.descr_txt::text').extract_first().strip(),
            'sourceLink' :
                 response.css('span.eventUrl a::attr(href)').extract_first()        
        }



            
                         
            
                         
