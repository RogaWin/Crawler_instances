# Scrapy settings for crawl_movies project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "crawl_movies"

SPIDER_MODULES = ["crawl_movies.spiders"]
NEWSPIDER_MODULE = "crawl_movies.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "crawl_movies (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Cookie':'richviews_9192=EMbVLczyCPFXROZsXcXHpcOO08dji69oYY%252BEpvNGjIgt4XtaxOJthIGASESDielNwQq170TCJdl8Jjy5M6NGjOqizuwrFdThumGN8lbY21pfl%252FzySB9eBWjGc6prrh0zcH4p8J3w2f9ac8JUnX3BRyG8jlOxqRHV2P5i6ZI4nTtKIAcVCCp40G%252BR3IAucIv5nVFGyfXOH9c1XX%252B95uPOYTOrT7c1nvikw2EiWghKjAtIsbLxg%252BevPe2N0JNwYghSWg0LQi%252ForPKMNdqGL2ENvdHB2%252FACyinD5lqOKRF0y4bMqauEJfy5YbifoAgCcXBXTX%252FT6NCoTYb18ZLC9OXkZw%253D%253D; 9192_3583_106.224.169.118=1; mediaKey=%7B%225817%22%3A1%2C%22timer%22%3A1719729608559%7D; beitouviews_9191=qYjgMyJt%252BKER39leGqXJ1Vt%252BuTIHCbiVLziHpzY9szilx%252BnbXCHD9%252B5E%252B5KJcMFiYb5%252FNPpZ%252B35wewVMZslLqPbYW3cjj9uQje%252BN0cbltGvSgKr0dJBEIR%252FQjhn8RHMMfTi%252B0WO114TSI2dTFr79Gny%252BAb1iyR3KOtEwl174PVCcOixZSvpZEGrNS7vGj4YQ68BcPRKkrT29DflHwpJTmuX6Z8thF%252B7FQPkLvz4cI6uH57%252B3vZpMoRz4qXKHDtgZyfs95k4Tj6OFVfKJyps2uTfSvIq49fvNG9xyTHSDN5IZSvatyD%252FvLk73P49IqxqV2HA1El4zt5PlfO7jODKgxA%253D%253D; 9191_3707_106.224.169.118=1',
    'Host':'dytt.dytt8.net',

}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "crawl_movies.middlewares.CrawlMoviesSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "crawl_movies.middlewares.CrawlMoviesDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "crawl_movies.pipelines.CrawlMoviesPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
