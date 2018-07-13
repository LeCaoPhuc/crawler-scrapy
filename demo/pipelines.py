# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from pymongo import MongoClient

MONGO_HOST = "mongodb://127.0.0.1"
MONGO_PORT = 27017
MONGO_DB = "genk"
MONGO_USER = "genkadmin"
MONGO_PASS = "123456"

def connect_db(db_name):
    con = MongoClient(MONGO_HOST,MONGO_PORT)
    db= con[MONGO_DB]
    db.authenticate(MONGO_USER,MONGO_PASS);

    return db
class CrawlerPipeline(object):
    def __init__(self):
        # self.collection = connect_db("genkData")["genkData"]
        print("testststststt");

    def process_item(self, item, spider):
        # self.collection.insert_one(item);
        print("connect_db =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--==--=-=-=-=-=-=-=-=-=-=-=-=-=-")

