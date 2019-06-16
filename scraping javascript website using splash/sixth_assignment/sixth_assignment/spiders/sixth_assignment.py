import scrapy
from scrapy_splash import SplashRequest


class QuoteToScrapeJsSpider(scrapy.Spider):
    name = 'quotesjs'

    def start_requests(self):
        yield SplashRequest(url='http://quotes.toscrape.com/js/', endpoint='render.html', callback=self.parse, args={'wait': 0.5})
    

    def parse(self, response):
        quotes = response.xpath("//div[@class='quote']")

        for quote in quotes:
            yield {
                "quote": quote.xpath(".//span[@class='text']/text()").extract_first(),
                "author": quote.xpath(".//span[2]/small/text()").extract_first(),
                "tags": quote.xpath(".//div[@class='tags']/a/text()").extract()
            }

        next_page = response.xpath("//li[@class='next']/a/@href").extract_first()

        if next_page:
            next_page_url = response.urljoin(next_page)
            yield SplashRequest(url=next_page_url, endpoint='render.html', callback=self.parse, args={'wait': 0.5})
