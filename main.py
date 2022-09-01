from twisted.internet.task import LoopingCall
from twisted.internet import reactor

from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

from MySpider import MySpider

configure_logging()
runner = CrawlerRunner()
task = LoopingCall(lambda: runner.crawl(MySpider))
task.start(60 * 5)
reactor.run()