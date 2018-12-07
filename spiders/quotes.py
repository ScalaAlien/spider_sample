# -*- coding: utf-8 -*-
import scrapy
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
import time


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ['www.google.co.jp']
    start_urls = ['https://www.google.co.jp/']
    proxy = 'proxy.fuku.sharp.co.jp:3080'
    proxy_auth = 's138093:refusethetemptationtoguess'
    options = ChromeOptions()
    options.add_argument('--proxy-server=http://%s' % proxy)
    options.add_argument('--proxy-auth=%s' % proxy_auth)
    options.add_argument('--headless')

    def start_requests(self):
        driver = Chrome(options=self.options)
        driver.get('https://www.google.co.jp/')
        input_search_form = driver.find_element_by_name('q')
        input_search_form.clear()
        input_search_form.send_keys('Python')
        input_search_form.send_keys(Keys.RETURN)

    def parse(self, response):
        print(response)
        pass
