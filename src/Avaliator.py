# coding: UTF-8


import requests
import re
from fake_useragent import UserAgent
import time


class Avaliator(object):

    def __init__(self, url):
        self.url = url


    def avaliate(self):
        link_clearing = lambda arg: re.sub('[\n]', '', arg)

        self.url = link_clearing(self.url)

        response = requests.head(self.url)

        if response.status_code != 404:
            return response.status_code

        else:
            raise ConnectionError


    def connect(self):
        # useragent = UserAgent()

        # header = {
        #     'Referer': '{}'.format(self.url),
        #     'User-Agent': '{}'.format(str(useragent.random))
        # }

        # time.sleep(5)

        response = requests.get(self.url)

        return response
