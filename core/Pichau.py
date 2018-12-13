from .Implements.ExtractorPichauImpl import ExtractorPichauImpl
from .Implements.ResultPichauImpl import ResultPichauImpl
from .Avaliator import Avaliator
from .Implements.HandlerPichauImpl import HandlerPichauImpl
from .TelegramIntegration.TelegramIntegrationPichau import TelegramIntegrationPichau
from .TelegramIntegration.Context import Context
from .Chart.ConcreteFactoryChart import ConcreteFactoryChart

'''
Design Pattern: Facade
'''

class Pichau(object):

  def __init__(self, link):
    self._database = HandlerPichauImpl('pichau')
    self._avaliator = Avaliator(link)
    self._extractor = None
    self._result = None
    self._telegram = Context(TelegramIntegrationPichau())

  def start(self):
    self._avaliator.avaliate()
    self._extractor = ExtractorPichauImpl(self._avaliator.connect())
    self._result = ResultPichauImpl(self._extractor.parser())

  def finish(self):
    self._telegram.context_interface(self._result.getResult())
    factory = ConcreteFactoryChart()    
    chartBar = factory.create_chart_bar()
    chartBar.interface_chart_bar(self._result.getResult())

    return self._result.getResultFormated()
