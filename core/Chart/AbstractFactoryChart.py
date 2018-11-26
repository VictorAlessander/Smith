import abc

'''
Design Pattern: Abstract Factory
'''

class AbstractFactoryChart(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create_chart_line(self):
        pass