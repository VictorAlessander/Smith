# coding: UTF-8

from ..Abstracts.AbstractResult import AbstractResult

@AbstractResult.register
class ResultKabumImpl(AbstractResult):

    def __init__(self, results):
        super(ResultKabumImpl, self).__init__()
        self.results = results

    def getResultFormated(self):
        return ("Produto: {}\nPreço Antigo: R$ {}\nPreço Atual: R$ {}\nÀ vista: R$ {}".format(
                self.results[0],
                self.results[1],
                self.results[2],
                self.results[3]))

    def getResult(self):
        return self.results
