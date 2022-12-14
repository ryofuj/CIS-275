'''
Ryo Fujimura
CIS 275C
Homework #4 Pt.2
'''

from AbstractCollection import AbstractCollection
from Array import Array

class PriorityQueue(AbstractCollection):
    def __init__(self, source_collection=None):
        self._items = Array(PriorityQueue.DEFAULT_CAPACITY)
        self._front = 0
        self._rear = 0
        AbstractCollection.__init__(self, source_collection)


    def add(self, item):
        if self._size == len(self._items):
            self.ensure_capacity(2 * len(self._items))
        self._items[self._rear] = item
        self._rear = (self._rear + 1) % len(self._items)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise KeyError("The queue is empty")
        old_item = self._items[self._front]
        self._front = (self._front + 1) % len(self._items)
        self._size -= 1
        return old_item

    def peek(self):
        if self.is_empty():
            raise KeyError("The queue is empty")
        return self._items[self._front]

    def __len__(self):
        return self._size