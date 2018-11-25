# coding: UTF-8

from ..Abstracts.AbstractResult import AbstractResult

@AbstractResult.register
class ResultPichauImpl(AbstractResult):

    def __init__(self, results):
        super(ResultPichauImpl, self).__init__()
        self.results = results

    def getResultFormated(self):
        return ("Produto: {}\nPreço Atual: R$ {}\nÀ vista: R$ {}".format(
                self.results[0],
                self.results[1],
                self.results[2]))

    def getResult(self):
        return self.results