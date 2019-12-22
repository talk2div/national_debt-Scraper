# -*- coding: utf-8 -*-
import scrapy


class GdpDeptSpider(scrapy.Spider):
    name = 'gdp_dept'
    allowed_domains = ['worldpopulationreview.com']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        row = response.xpath('//table[@class="table table-striped"]/tbody/tr')
        for each_row in row:
            name = each_row.xpath('.//td[1]/a/text()').get()
            gdp_dept = each_row.xpath('.//td[2]/text()').get()

            yield{
                "country_name":name,
                "gdp_dpt":gdp_dept
            }
