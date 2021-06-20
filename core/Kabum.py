from .Implements.ExtractorKabumImpl import ExtractorKabumImpl
from .Implements.ResultKabumImpl import ResultKabumImpl
from .Avaliator import Avaliator
from .TelegramIntegration.TelegramIntegrationKabum import TelegramIntegrationKabum
from .TelegramIntegration.Context import Context

"""
Design Pattern: Facade
"""


class Kabum(object):
    def __init__(self, link):
        # self.database
        self._avaliator = Avaliator(link)
        self._extractor = None
        self._result = None
        self._telegram = Context(TelegramIntegrationKabum())

    def start(self):
        self._avaliator.avaliate()
        self._extractor = ExtractorKabumImpl(self._avaliator.connect())
        self._result = ResultKabumImpl(self._extractor.parser())

    def finish(self):
        self._telegram.context_interface(self._result.getResult())

        return self._result.get_results_formated()
