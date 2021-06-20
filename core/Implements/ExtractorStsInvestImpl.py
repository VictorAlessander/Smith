from bs4 import BeautifulSoup as BSoup
import re
from ..Abstracts.AbstractExtractor import AbstractExtractor
from decimal import Decimal


@AbstractExtractor.register
class ExtractorStsInvestImpl(AbstractExtractor):
    def __init__(self, response):
        super(ExtractorStsInvestImpl, self).__init__()
        self.response = response

    @staticmethod
    def special_characters_remover(value):
        return re.sub("[\t\n M]", "", value)

    @staticmethod
    def dot_remover(value):
        return re.sub("[.]", "", value)

    @staticmethod
    def comma_handler(value):
        return re.sub("[,]", ".", value)

    def sanitize_currency_value(self, value):
        special_characters_removed = self.special_characters_remover(value)
        dot_removed = self.dot_remover(special_characters_removed)
        comma_handled = self.comma_handler(dot_removed)
        return Decimal(comma_handled)

    def parser(self):
        results = []
        gross_profit_sanitized = []
        operating_costs_sanitized = []

        content = BSoup(self.response.text, "html.parser")

        dre_table = content.find(
            "div",
            attrs={
                "aria-label": "Grid com a demonstração do resultado do exercício (DRE)"
            },
        )

        dre_table_body = dre_table.find("tbody")

        gross_profit = dre_table_body.select("tr")[2]
        operating_costs = dre_table_body.select("tr")[3]

        for gross_profit_elements in gross_profit.find_all(
            "td", attrs={"class": "level-0 value text-right DATA "}
        ):
            gross_profit_value = gross_profit_elements.find(
                "span", attrs={"class": "d-block"}
            )
            gross_profit_sanitized.append(
                self.sanitize_currency_value(gross_profit_value.text)
            )

        for operating_costs_elements in operating_costs.find_all(
            "td", attrs={"class": "level-0 value text-right DATA "}
        ):
            operating_costs_value = operating_costs_elements.find(
                "span", attrs={"class": "d-block"}
            )
            operating_costs_sanitized.append(
                self.sanitize_currency_value(operating_costs_value.text)
            )

        results.append(gross_profit_sanitized)
        results.append(operating_costs_sanitized)

        gross_profit_sanitized_size = len(gross_profit_sanitized)
        operating_costs_sanitized_size = len(operating_costs_sanitized)

        operating_revenue_profit_values = []
        company_ticker = str.upper(self.response.url.split("/")[4])

        if gross_profit_sanitized_size == operating_costs_sanitized_size:
            for x in range(0, gross_profit_sanitized_size):
                operating_revenue_profit_values.append(
                    gross_profit_sanitized[x] - abs(operating_costs_sanitized[x])
                )

        data_collected = dict(
            company=company_ticker,
            operating_revenue_profit_values=operating_revenue_profit_values,
        )

        return data_collected
