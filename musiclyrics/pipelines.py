# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import threading
import sys


class MusiclyricsPipeline(object):
	lock = threading.Lock()
	file = open("music.json",'a')
	
	def __init__(self):
		pass

	def process_item(self,item,spider):
		line = json.dumps(dict(item))+'\n'
		try:
			MusiclyricsPipeline.lock.acquire()	
			MusiclyricsPipeline.file.write(line)
		except:
			pass
		finally:
		 	MusiclyricsPipeline.lock.release()
		return item
