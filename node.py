class Node:
    def __init__(self, data=None):
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data

    @data.setter 
    def data(self, data):
        self._data = data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next
