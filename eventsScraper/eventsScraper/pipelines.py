# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class EventsscraperPipeline(object):
    def __init__(self):
       #Connect to database and assign to conn 
        conn = sqlite3.connect('../../eventsApp/db.sqlite3')

    #Function that process item by placing them into sqlite3 database
    def process_item(self, item, spider):
        #set up cursor
        cursor = conn.cursor()
        # Create insert query and pass the data from item array parameter
        insertEvent = ("INSERT INTO Event (title, desc, price, priceText, venue, date, dateText, imgLoc, category,
        originURL)"
        "VALUES (%s, %s, %d, %s, %s, %s, %s, %s, %s)")
        data = ((item['title'][0].encode('utf-8')),
                (item['desc'][0].encode('utf-8')),
                (item['price'][0].encode('utf-8')),
                (item['priceText'][0].encode('utf-8')),
                (item['venue'][0].encode('utf-8')),
                (item['date'][0].encode('utf-8')),
                (item['dateText'][0].encode('utf-8')),
                (item['imgLoc'][0].encode('utf-8')),
                (item['category'][0].encode('utf-8')),
                (item['originURL'][0].encode('utf-8')))

        #Execute insert query and close cursor and connection
        cursor.execute(insertEvent, data)
        conn.commit()
        cursor.close()
        conn.close()

        #Define and exception caused by sqlite3 error
        except sqlite3.Error as e:
        print "SQLite3 error %s", e
        conn.close()
       
       return item

    def spider_close(self, spider):
        conn.close()
