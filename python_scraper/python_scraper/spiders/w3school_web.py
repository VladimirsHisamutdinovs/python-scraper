import scrapy


class W3schoolWebSpider(scrapy.Spider):
    name = 'w3school_web'
    allowed_domains = ['www.w3schools.com']
    start_urls = ['http://www.w3schools.com/html']

    def parse(self, response):
        for link in response.css('div.w3-sidebar a::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_articles)

    def parse_articles(self, response):
        articles = response.css('div.w3-row')
        for article in articles:
            yield {
                'title':article.css('h1::text').get(),
                #'subtitle':article.css('h2::text').getall()
                # 'h2_subtitle':article.css('h2::text').get(),
                # 'h3_subtitle':article.css('h3::text').get(),
                'article_body':article.css('p::text').getall(),
                #'article_code':article.css('div.w3-code::text').getall()
            }
