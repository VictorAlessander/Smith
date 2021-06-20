from core.Implements.ResultStsInvestImpl import ResultStsInvestImpl
from core.Implements.ExtractorStsInvestImpl import ExtractorStsInvestImpl
from .Avaliator import Avaliator
from .Chart.StsInvestConcreteChartBar import StsInvestConcreteChartBar


class StatusInvest:
    def __init__(self, tickers):
        self.tickers = tickers
        self._database = None
        self._avaliator = None
        self._extrator = None
        self._result = None

    def start(self):
        results = []
        for ticker in self.tickers:
            link = f"https://statusinvest.com.br/acoes/{ticker}"
            self._avaliator = Avaliator(link)
            self._avaliator.avaliate()
            self._extractor = ExtractorStsInvestImpl(self._avaliator.connect())
            results.append(self._extractor.parser())

        self._result = ResultStsInvestImpl(results)

    def finish(self):
        factory = StsInvestConcreteChartBar()
        factory.interface_chart_bar(self._result.get_results())

        return None
