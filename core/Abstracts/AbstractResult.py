import abc

class AbstractResult(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getResultFormated(self):
        pass
