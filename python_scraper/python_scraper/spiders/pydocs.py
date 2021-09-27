import scrapy
import re


class PydocsSpider(scrapy.Spider):
    name = 'pydocs'
    allowed_domains = ['docs.python.org']
    start_urls = ['https://docs.python.org/3/tutorial/index.html']

    def parse(self, response):
        for link in response.css('div.bodywrapper a::attr(href)',):
            yield response.follow(link.get(), callback=self.parse_articles)

    def parse_articles(self, response):
        articles = response.css('div.body')
        for article in articles:
            yield {
                'title':article.css('h1::text').get(),
                # 'h2_subtitle':article.css('h2::text').get(),
                # 'h3_subtitle':article.css('h3::text').get(),
                'article_body':article.css('p::text').getall()
                #'article_code':article.css('span::text').getall()
                #'article_code':article.css('div.highlight::text').getall()
            }

            ## run with: scrapy crawl pydocs -o name.csv 
            ## generate spider with: scrapy genspider {spider name} {base URL of the resourse we want to scrap}
            ## start scrapy project with: scrapy startproject {projectname}