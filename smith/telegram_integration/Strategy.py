import abc

'''
Design Pattern: Strategy
'''

class Strategy(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def send(self):
        pass