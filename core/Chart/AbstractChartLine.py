import abc

'''
Design Pattern: Abstract Factory
'''

class AbstractChartLine(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def interface_chart_line(self):
        pass