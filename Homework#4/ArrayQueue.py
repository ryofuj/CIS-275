'''
Ryo Fujimura
CIS 275C
Homework #4
'''

from AbstractCollection import AbstractCollection
from Array import Array

class ArrayQueue(AbstractCollection):
    DEFAULT_CAPACITY = 10

    def __init__(self, source_collection=None):
        self._items = Array(ArrayQueue.DEFAULT_CAPACITY)
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
        self._items = Array(ArrayQueue.DEFAULT_CAPACITY)

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
        self._rear = self._size

    def print_queue(self):
        if self.is_empty():
            print("The queue is empty")
        else:
            cursor = self._front
            while cursor != self._rear:
                print(self._items[cursor])
                cursor = (cursor + 1) % len(self._items)

if __name__ == "__main__":
    q = ArrayQueue()
    for i in range(15):
        q.add(i)
    q.print_queue()
    print("Pop.")
    for i in range(15):
        print(q.pop())
    print("Add.")
    for i in range(15):
        q.add(i)
    q.print_queue()
    print("Peek.")
    for i in range(15):
        print(q.peek())
        q.pop()


