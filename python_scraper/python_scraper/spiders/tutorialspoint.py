import scrapy


class TutorialspointSpider(scrapy.Spider):
    name = 'tutorialspoint'
    allowed_domains = ['www.tutorialspoint.com']
    start_urls = ['https://www.tutorialspoint.com/html']

    def parse(self, response):
        for link in response.css('div.mui-col-md-3 a::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_articles)

    def parse_articles(self, response):
        articles = response.css('div.mui-col-md-6')
        for article in articles:
            yield {
                'title':article.css('h1::text').get(),
                #'subtitle':article.css('h2::text').getall()
                # 'h2_subtitle':article.css('h2::text').get(),
                # 'h3_subtitle':article.css('h3::text').get(),
                'article_body':article.css('p::text').getall()
                # 'article_code':article.css('div.demo-view::text').getall()
            }
