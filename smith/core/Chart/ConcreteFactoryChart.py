from .AbstractFactoryChart import AbstractFactoryChart
from .ConcreteChartLine import ConcreteChartLine
from .ConcreteChartBar import ConcreteChartBar


'''
Design Pattern: Abstract Factory
'''

class ConcreteFactoryChart(AbstractFactoryChart):

    def create_chart_line(self):
        return ConcreteChartLine()
    
    def create_chart_bar(self):
        return ConcreteChartBar()