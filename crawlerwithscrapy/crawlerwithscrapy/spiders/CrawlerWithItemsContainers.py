import scrapy

from ..items import CrawlerwithscrapyItem


class WebCrawler(scrapy.Spider):
    name = "quots"

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        items=CrawlerwithscrapyItem()       #Instance from the class CrawlerwithscrapyItem
        for quote in response.css('div.quote'):

                text= quote.css('span.text::text').extract()
                author= quote.css('small.author::text').extract()
                tags= quote.css('div.tags a.tag::text').extract()

                items['text']=text
                items['author']=author
                items['tags']=tags

                yield items
