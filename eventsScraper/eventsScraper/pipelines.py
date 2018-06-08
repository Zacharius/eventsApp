# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class EventsscraperPipeline(object):
    
    def open_spider(self, spider):
        self.conn = sqlite3.connect('../../eventsApp/db.sqlite3')

    def close_spider(self, spider):
        self.conn.close

    #Function that process item by placing them into sqlite3 database
    def process_item(self, item, spider):
        #set up cursor

        try: 
            cursor = self.conn.cursor()
            # Create insert query and pass the data from item array parameter
            insertEvent = ("INSERT INTO cal_event (title, desc, price, priceText,"
                           "venue, date, dateText, imgLoc, category, sourceLink,"
                            "slug)"
                            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")
            data = ((item['title']),
                    (item['desc']),
                    (item['price']),
                    (item['priceText']),
                    (item['venue']),
                    (constructDateTime(item['date'])),
                    (item['dateText']),
                    (item['imgLoc']),
                    (item['category']),
                    (item['sourceLink']),
                    (reduceToSlug(item['title'])))
            

            #Execute insert query and close cursor and connection
            cursor.execute(insertEvent, data)
            self.conn.commit()
            cursor.close()

            #Define and exception caused by sqlite3 error
        except sqlite3.Error as e:
            print("SQLite3 error:: %s", e)
            cursor.close()
       
        return item

    def spider_close(self, spider):
        conn.close()

#remove all non-alphanumerics from title, replace spaces with underscore, makes
#lower case

def reduceToSlug(title):

    title = title.lower()
    
    slug = ""

    for char in title:
        if char.isspace():
            slug += "_"

        if char.isalnum():
            slug += char

    return slug


def constructDateTime(dateText):


    #if dateText is empty, return nothing
    if not dateText:
        return

    dateText = dateText.lower()
    
    #associative array mapping month names to their corresponding number
    monthStringToNum = {
        "january" : '01',
        "jan." : '01',
        "february" : '02',
        "feb." : '02',
        "march" : '03',
        "mar." : '03',
        "april" : '04',
        "apr." : '04',
        "may." : '05',
        "june" : '06',
        "jun." : '06',
        "july" : '07',
        "jul." : '07',
        "august" : '08',
        "aug." : '08',
        "september" : '09',
        "sept." : '09',
        "october" : '10',
        "oct." : '10',
        "november" : '11',
        "nov." : '11',
        "december" : '12' ,
        "dec." : '12' }


    month = monthStringToNum[dateText.split(" ")[0]]
    day = dateText.split(" ")[1]

    if not len(day)==2:
        day = "0"+day

    return "2018-"+month+"-"+day+" 00:00:00"

