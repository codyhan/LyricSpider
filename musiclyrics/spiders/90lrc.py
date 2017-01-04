#encoding=utf-8
import scrapy
from musiclyrics.items import MusiclyricsItem
import json
import time 
import re
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
class LycSpider(CrawlSpider):
	name = 'lyc'
	start_urls=['http://www.90lrc.cn']
	base_url='http://www.90lrc.cn'
	allowed_domains=['90lrc.cn']
 	rules=[Rule(SgmlLinkExtractor(allow=('/[0-9]{5,10}/.*$'),restrict_xpaths=('//li')),callback="parseLyrics",follow=True),Rule(SgmlLinkExtractor(allow=('/geshou/.*$'),restrict_xpaths=('//li')),callback="parseSonger",follow=True)]
	def parseLyrics(self,response):
		data = response.xpath("//div[@class='lyric']")
		item = MusiclyricsItem()
		url = response.url
		title = data.xpath("//li")[3].xpath(".//a/text()").extract()
		author = data.xpath("//li")[5].xpath(".//a/text()").extract()
		content = data.xpath("//li[@id='txt']/text()").extract()
		#if len(url)!=0 and len(title)!=0 and len(author)!=0 and len(content)!=0:
		if len(url)!=0 and len(content)!=0:
			item['url']=url
			item['title']=title[0]
			item['author']=author[0]
			item['content']=content[0]
			yield item
	def parseSonger(self,response):
		urls = response.xpath("//a/@href").extract()
		for url in urls:
			if len(re.findall(r"[0-9]{5,10}",url))!=0:
				url = self.base_url+url
				yield scrapy.Request(url,self.parseLyrics)
		
"""
	def parse(self, response):

"""
	
