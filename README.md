An event aggregater, allows you to see whats going on around San Antonio.

The website can be found at https://eventnear.us

This is an ongoing project by several developers to make a fully featured event website that allows you to search, interact, and receive content in interesting and intuitive ways. Our hope with this project is to better learn and practice our UI and engineering skills, get exposed to new technologies/frameworks, and to provide a tool that will be valuable to our community.


To Run Webscraper:

   For webscraping we are using the python library Scrapy. Ensure you have this
   package installed before attempting this.


   1. from project root, navigate to eventsScrapper/eventsScraper.

      	   $cd eventsScrapper/eventsScraper

   2. copy the default settings file, .settings.py, into your own settings file,
   settings.py.

           $cp ,settings.py settings.py


    3. Run whatever spider you want to use, with the command scrapy . Currently the
    only fully operational spider is theCurrent.

    	   $scrapy crawl theCurrent

   