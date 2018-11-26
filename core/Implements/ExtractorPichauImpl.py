# coding: UTF-8

from bs4 import BeautifulSoup as BSoup
import re
from ..Abstracts.AbstractExtractor import AbstractExtractor

@AbstractExtractor.register
class ExtractorPichauImpl(AbstractExtractor):

    def __init__(self, response):
        super(ExtractorPichauImpl, self).__init__()
        self.response = response


    def parser(self):
        results = []

        content = BSoup(self.response.text, "html.parser")

        name = content.find('div', attrs={'class': 'product title'})
        normal_price = content.find('span', attrs={'class': 'price'})
        in_cash = content.find('span', attrs={'class': 'price-boleto'})

        filtrator = lambda arg: re.sub('[\t\nDdeporàvistanoboletocomdesconto R$]', '', arg)

        if name is not None:
            name = content.find('h1').text

        if normal_price is not None:
            normal_price = normal_price.text
            normal_price = ".".join(normal_price.split(','))
            normal_price = filtrator(normal_price)

        if in_cash is not None:
            in_cash = in_cash.find('span').text
            in_cash = ".".join(in_cash.split(','))
            in_cash = filtrator(in_cash)

        results.append(name)
        results.append(normal_price)
        results.append(in_cash)

        return results
