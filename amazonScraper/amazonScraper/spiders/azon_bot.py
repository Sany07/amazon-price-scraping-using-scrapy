import scrapy

from ..items import AmazonscraperItem

class AmazonBotSpider(scrapy.Spider):
    name = 'azon-bot'
    start_urls = [

        "https://www.amazon.com/s?k=iphone&page=1&qid=1624792241&ref=sr_pg_2"    
        # 'http://quotes.toscrape.com/page/1/',           
        ]

    def parse(self, response):
        
        product=AmazonscraperItem()
        
        for q in response.css('div.a-section'):

            name=q.css("span.a-text-normal::text").get()
            price=q.css("span.a-price-whole::text").get()   

            if name and price:
                product["name"]=name
                product["price"]=price

                yield product
