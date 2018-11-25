# coding: UTF-8

from bs4 import BeautifulSoup as BSoup
import re
from ..Abstracts.AbstractExtractor import AbstractExtractor

@AbstractExtractor.register
class ExtractorKabumImpl(AbstractExtractor):

    def __init__(self, response):
        super(ExtractorKabumImpl, self).__init__()
        self.response = response


    def parser(self):
        results = []

        content = BSoup(self.response.text, "html.parser")

        name = content.find('div', attrs={'id': 'titulo_det'})
        old_price = content.find('div', attrs={'class': 'preco_antigo'})
        normal_price = content.find('div', attrs={'class': 'preco_normal'})
        in_cash = content.find('span', attrs={'itemprop': 'offers'})

        filtrator = lambda arg: re.sub('[\t\nDdepor R$]', '', arg)

        if name is not None:
            name = content.find('h1', attrs={'class': 'titulo_det'}).text

        if old_price is not None:
            old_price = old_price.text
            old_price = ".".join(old_price.split(','))
            old_price = filtrator(old_price)

        if normal_price is not None:
            normal_price = normal_price.text
            normal_price = ".".join(normal_price.split(','))
            normal_price = filtrator(normal_price)

        if in_cash is not None:
            in_cash = in_cash.text
            in_cash = ".".join(in_cash.split(','))
            in_cash = filtrator(in_cash)

        results.append(name)
        results.append(old_price)
        results.append(normal_price)
        results.append(in_cash)

        return results