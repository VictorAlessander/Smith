import abc

class AbstractHandler(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create_database(self):
        pass

    @abc.abstractmethod
    def store_database(self):
        pass
