"""
Design Pattern: Strategy
"""


class Context(object):
    def __init__(self, strategy):
        self._strategy = strategy

    def context_interface(self, data):
        self._strategy.send(data)
