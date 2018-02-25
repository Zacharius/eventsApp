# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import sys
import hashlib
import MYSQLdb
#from scrapy.extensions import DropItem
from scrapy.http import Request




class ViacalPipeline(object):
    def __init__(self):
        conn = mysqldb.connector.connect(host=os.environ['RDS_HOSTNAME'],
            database=os.environ['RDS_DB_NAME'],
            user=os.environ['RDS_USERNAME'],
            password=os.environ['RDS_PASSWORD'])



    def process_item(self, item, spider):
        try:
            self.cursor("""INSERT INTO Events (date, ename, hname, description, address, cost, startTime, tags, dow)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                            (item['date'].encode('utf-8')), 
                            (item['title'].encode('utf-8')),
                            (item['venue'].encode('utf-8')),
                            (item['des'].encode('utf-8')),
                            (item['address'].encode('utf-8')), 
                            (item['cost'].encode('utf-8')),
                            (item['time'].encode('utf-8')),
                            (item['cats'].encode('utf-8')),
                            (item['dow'].encode('utf-8')))

            self.conn.commit()

        except MYSQLdb.Error, e:
            self.conn.commit()
            print "MYSQL Error %d: %s" % (e.args[0], e.args[1])

        return item
