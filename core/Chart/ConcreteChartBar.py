from .AbstractChartBar import AbstractChartBar
import plotly as py
import plotly.graph_objs as go

'''
Design Pattern: Abstract Factory
'''

class ConcreteChartBar(AbstractChartBar):

    def interface_chart_bar(self, data):
        content = [go.Bar(
            x=[data[0]],
            y=[data[1]]
        )]

        py.offline.plot(content, filename='comparative')