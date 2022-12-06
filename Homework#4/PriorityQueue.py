'''Although we've seen a linked-list based priority queue, the most efficient PriorityQueue implementation uses a heap for its internal data. Create a PriorityQueue class which prioritizes the smallest entry, which should be relatively simple:

    It should inherit from AbstractCollection
    In the constructor, create an attribute which is a MinHeap to store the priority queue's data. You may include the MinHeap code included in this week's lab prompt.
    Add three more methods: pop, peek, and add. Each should simply pop from, peek at, or add to the internal MinHeap.
    The item at the top of the MinHeap will always be the smallest item. We can visualize the top of the heap as being the front of the priority queue.
'''

'''
Ryo Fujimura
CIS 275C
Homework #4 Pt.2
'''

from AbstractCollection import AbstractCollection
from Array import Array

class PriorityQueue(AbstractCollection):
    DEFAULT_CAPACITY = 10

    def __init__(self, source_collection=None):
        self._items = Array(PriorityQueue.DEFAULT_CAPACITY)
        self._front = 0
        self._rear = 0
        AbstractCollection.__init__(self, source_collection)

    def __iter__(self):
        cursor = self._front
        while cursor != self._rear:
            yield self._items[cursor]
            cursor = (cursor + 1) % len(self._items)

    def clear(self):
        self._size = 0
        self._front = 0
        self._rear = 0
        self._items = Array(PriorityQueue.DEFAULT_CAPACITY)

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

    def ensure_capacity(self, new_capacity):
        if new_capacity < self._size:
            return
        old = self._items
        self._items = Array(new_capacity)
        cursor = self._front
        for count in range(self._size):
            self._items[count] = old[cursor]
            cursor = (cursor + 1) % len(old)
        self._front = 0

        