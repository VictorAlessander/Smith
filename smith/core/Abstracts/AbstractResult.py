import abc


class AbstractResult(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_results_formated(self):
        pass
