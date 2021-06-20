from ..Abstracts.AbstractResult import AbstractResult


@AbstractResult.register
class ResultStsInvestImpl(AbstractResult):
    def __init__(self, results):
        super(ResultStsInvestImpl, self).__init__()
        self.results = results

    # def normalize_results(self):
    #     companies = []
    #     data_values = []
    #     for result in self.results:
    #         companies.append(result.get("company"))
    #         data_values.append(result.get("operating_revenue_profit_values"))

    #     normalized = dict(companies=companies, data_values=data_values)

    #     import pdb

    #     pdb.set_trace()

    #     return normalized

    def get_results(self):
        return self.results

    def get_results_formated(self):
        pass
