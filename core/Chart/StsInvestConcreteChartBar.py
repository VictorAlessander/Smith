from .AbstractChartBar import AbstractChartBar

import plotly as py
import plotly.graph_objects as go

import pandas as pd

# import plotly.express as px

"""
Design Pattern: Abstract Factory
"""


class StsInvestConcreteChartBar(AbstractChartBar):
    def interface_chart_bar(self, data):
        # df = pd.DataFrame(
        #     {
        #         "Year": ["2020", "2019", "2018", "2017", "2016"],
        #         "Ticker": data.get("company"),
        #         "Operating Revenue Profit": data.get("data_values"),
        #     }
        # )

        # fig = px.bar(
        #     df,
        #     x="Year",
        #     y="Operating Revenue Profit",
        #     barmode="group",
        #     title="Comparative (values in R$ Millions)",
        #     color="Ticker",
        # )

        fig = go.Figure(
            data=[
                go.Bar(
                    name=element.get("company"),
                    x=["2020", "2019", "2018", "2017", "2016"],
                    y=element.get("operating_revenue_profit_values"),
                )
                for element in data
            ]
        )

        fig.update_layout(barmode="group")

        # fig.show()

        # content = [go.Bar(x=[2020, 2019, 2018, 2017, 2016], y=data)]

        py.offline.plot(fig, filename="operating_revenue_profit.html")
