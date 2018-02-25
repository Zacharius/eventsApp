# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import sys
import hashlib
import mysql.connector 
from mysql.connector import errorcode 
#from scrapy.extensions import DropItem
from scrapy.http import Request
from datetime import datetime



class ViacalPipeline(object):
    def __init__(self):
        conn = mysql.connector.connect(host=os.environ['RDS_HOSTNAME'],
            database='viaSocial',
            user=os.environ['RDS_USERNAME'],
            password=os.environ['RDS_PASSWORD'])



    def process_item(self, item, spider):
        
        try:
            conn = mysql.connector.connect(host=os.environ['RDS_HOSTNAME'],
            database='viaSocial',
            user=os.environ['RDS_USERNAME'],
            password=os.environ['RDS_PASSWORD'])
            
            preDate = item['date'][0]
            preDate = preDate.strip('\n')
            preDate = preDate.strip()
            dateR = preDate + ", 2018"
            dateU = dateR.encode("utf-8")
            dt_obj = datetime.strptime(dateU,'%b %d, %Y')
            #dateI = dt_obj.strftime('%b %d, %Y')
            dateF = dt_obj.strftime('%Y-%m-%d')
            print(dateF)
            print('*******************************************************')


            cursor = conn.cursor()
            insertEvent = ("INSERT IGNORE INTO Events (date, ename, hname, description, address, cost, " 
                            "startTime) "
                            "VALUES (%s, %s, %s, %s, %s, %s, %s)" )

            data = ((dateF.encode('utf-8')), 
                    (item['title'][0].encode('utf-8')),
                    (item['venue'][0].encode('utf-8')),
                    (item['des'][0].encode('utf-8')),
                    (item['address'][0].encode('utf-8')), 
                    (item['cost'][0].encode('utf-8')),
                    (item['time'][0].encode('utf-8')))

            cursor.execute(insertEvent, data)
            conn.commit()
            cursor.close()
            conn.close()

        except mysql.connector.Error as  e:
            print "MYSQL Error %s", e
            conn.close()


        return item

    def spider_close(self, spider):
       conn.close()
