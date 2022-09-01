from dataclasses import dataclass, field
from typing import Optional
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose, Join
#import sys

@dataclass(eq=True, unsafe_hash=True)
class Product:
    name: Optional[str] = field(default=None)
    price: Optional[float] = field(default=None)
    availability: Optional[bool] = field(default=None)

class ProductLoader(ItemLoader):

    default_output_processor = TakeFirst()

    price_in = MapCompose(lambda v: float(v))

class MySpider(scrapy.Spider):
    name = 'micromania.fr'
    allowed_domains = ['micromania.fr']
    start_urls = [
        'https://www.micromania.fr/consoles-ps5.html',
    ]
    custom_settings = {
        'ITEM_PIPELINES' : {
            'pipeline.AvailabilityPipeline.AvailabilityPipeline': 100,
            'pipeline.PricePipeline.PricePipeline': 200,
            'pipeline.MailSenderPipeline.MailSenderPipeline': 300,
        },
        'RETRY_ENABLED' : True,
        'RETRY_TIMES' : 10000,
        'LOG_LEVEL' : 'INFO',
        'LOG_FORMATTER' : 'logformatter.PoliteLogFormatter'
    }

    def parse(self, response):
        for productDiv in response.css('div.product-column'):
            name = 'div.product-name a[data-gtm]::text'
            price = 'span.sales span[itemprop]::attr(content)'
            availability = productDiv.css('link[href="http://schema.org/InStock"]').get() != None
            
            l = ProductLoader(item=Product(), selector=productDiv)
            l.add_css('name', name)
            l.add_css('price', price)
            l.add_value('availability',availability)
            yield l.load_item()

#process = CrawlerProcess()
#process.crawl(MySpider)
#process.start()