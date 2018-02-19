import scrapy

class QuotesSpider(scrapy.Spider):
    name = "cerpenmu"

    def start_requests(self):
        urls = [
            'http://cerpenmu.com/cerpen-cinta/seteguk-harapan.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for page in response.css('.post > p')[:-3]:
            yield {
                'text' : page.extract()
            }

        next_page = response.css('.featured-title > a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)