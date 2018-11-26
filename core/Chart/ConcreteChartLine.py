from .AbstractChartLine import AbstractChartLine
import plotly as py
import plotly.graph_objs as go

'''
Design Pattern: Abstract Factory
'''

class ConcreteChartLine(AbstractChartLine):

    def interface_chart_line(self, data):
        trace1 = go.Scatter(
            x=['Pichau'],
            y=[data[1], data[2]],
            name=data[0]
        )

        trace2 = go.Scatter(
            x=['Kabum'],
            y=[300, 249.99],
            name=data[0]
        )

        content = [trace1, trace2]
        layout = go.Layout(
            title='Smith Chart'
        )

        fig = go.Figure(data=content, layout=layout)
        plot_url = py.offline.plot(fig, filename='comparative')