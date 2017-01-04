# -*- coding: utf-8 -*-

# Scrapy settings for musiclyrics project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'musiclyrics'

SPIDER_MODULES = ['musiclyrics.spiders']
NEWSPIDER_MODULE = 'musiclyrics.spiders'
DOWNLOAD_DELAY = 3
RANDOMIZE_DOWNLOAD_DELAY = True
DOWNLOADER_MIDDLEWARES = {
	'musiclyrics.middlewares.MyCustomDownloaderMiddleware': None,
	'musiclyrics.rotateuseragent.RotateUserAgentMiddleware':400
}


ITEM_PIPELINES = {
    'musiclyrics.pipelines.MusiclyricsPipeline': 300,
}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'musiclyrics (+http://www.yourdomain.com)'
