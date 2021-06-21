import abc

class AbstractExtractor(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def parser(self):
        pass
