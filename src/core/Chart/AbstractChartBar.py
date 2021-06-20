import abc

'''
Design Pattern: Abstract Factory
'''

class AbstractChartBar(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def interface_chart_bar(self):
        pass