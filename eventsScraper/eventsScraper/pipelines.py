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

    #associative array mapping month names to their corresponding number
    monthStringToNum = {
        "January" : '01',
        "Jan." : '01',
        "February" : '02',
        "Feb." : '02',
        "March" : '03',
        "Mar." : '03',
        "April" : '04',
        "Apr." : '04',
        "May." : '05',
        "June" : '06',
        "Jun." : '06',
        "July" : '07',
        "Jul." : '07',
        "August" : '08',
        "Aug." : '08',
        "September" : '09',
        "Sept." : '09',
        "October" : '10',
        "Oct." : '10',
        "November" : '11',
        "Nov." : '11',
        "December" : '12' ,
        "Dec." : '12' }


    month = monthStringToNum[dateText.split(" ")[0]]
    day = dateText.split(" ")[1]

    if not len(day)==2:
        day = "0"+day

    return "2018-"+month+"-"+day+" 00:00:00"

