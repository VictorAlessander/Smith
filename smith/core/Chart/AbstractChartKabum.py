import abc

'''
Design Pattern: Abstract Factory
'''

class AbstractChartKabum(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def interface_chart_kabum(self):
        pass