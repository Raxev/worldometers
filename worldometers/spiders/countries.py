import scrapy
import logging

logger = logging.getLogger(__name__)


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response, **kwargs):
        countries = response.xpath("//td/a")
        for country in countries:
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()
            # absolute_url = f"https://www.worldometers.ifno{link}"
            # absolute_url = response.urljoin(link)
            yield response.follow(url=link, callback=self.parse_country, meta={'country_name': name})


    @staticmethod
    def parse_country(response, **kwargs):
        name = response.request.meta['country_name']
        rows = response.xpath('(//table[@class="table table-striped table-bordered table-hover table-condensed table-list"])[1]/tbody/tr')
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()
            yield {
                'country_name': name,
                'year': year,
                'population': population
            }


class GdpDebtSpider(scrapy.Spider):
    name = 'gdp_debt'
    allowed_domains = ['worldpopulationreview.com']
    start_urls = ['https://worldpopulationreview.com/countries/countries-by-national-debt']

    def parse(self, response, **kwargs):
        countries = response.xpath("//tr/td/a')]")
        for country in countries:
            country_name = country.xpath(".//td[1]/a/text()").get()
            gdp_debt = country.xpath(".//td[2]/text()").get()
            population = country.xpath(".//td[3]/text()").get()

            yield {
                'country_name': country_name,
                'gdp_debt': gdp_debt,
                'population': population
            }
