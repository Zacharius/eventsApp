import scrapy

class theCurrentEventsSpider(scrapy.Spider):
    name= "theCurrent"

    start_urls = [
        "https://www.sacurrent.com/sanantonio/EventSearch"
    ]


    #root parsing method, begins parsing at start_urls
    def parse(self, response):

        #grab and parse all listings on first page
        #eventPages = response.css('div.listing > h3 > a::attr(href)').extract()

        
        #for eventPage in eventPages :
        #    yield scrapy.Request(eventPage, callback=self.parseEvent)
                                     
    
        #find out how many pages of events there are
        numPages = response.css('div.pagination a::attr(title)').re(r'\d+$')[0]


        #go through every page and parse the events contained within
        for page in range(1, int(numPages)+1):
            eventPage = response.urljoin('?page='+str(page))
            yield scrapy.Request(eventPage, callback=self.parseEventPage)
            
            
    def parseEventPage(self, response):
        
         #grab and parse all events on the page
        eventPages = response.css('div.listing > h3 > a::attr(href)').extract()

        
        for eventPage in eventPages :
            yield scrapy.Request(eventPage, callback=self.parseEvent)   


    def parseEvent(self, response):

        titleList = response.css('h1.listingTitle::text')

        title = titleList[len(titleList)-1].extract().strip()

        dateText = response.css('span.eventWhen::text').extract_first().strip()

        date = response.css('span.eventWhen::text').re(r'\w+\.* \d+')[0]

        priceHTML =   response.css('span.eventPrice::text')

        if priceHTML:
            priceText = priceHTML.extract_first().strip()
        else:
            priceText = 'Free'
        

        if priceText == 'Free':
            price = 0
        else:
            price = response.css('span.eventPrice::text').re(r'\d+')[0]

        descriptions = response.css('div.descr_txt *::text').extract()
        # peice together all parts of description, sometimes description has
        # embedded tags
        desc = ""
        for i in descriptions:
          desc += i.strip()+ " "
          
        sourceLink = response.css('span.eventUrl a::attr(href)').extract_first()

        imgLoc = \
        response.css('link[rel="image_src"]::attr(href)').extract_first()

        categoryHTML = response.css('p.tags a::text')

        if categoryHTML:
            category = categoryHTML.extract_first()
        else:
            category = 'none'
        
        venue = response.css('li.locationItem h4 a::text').extract_first()

        if title:
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

    

    
            
        

            
                         
            
                         
