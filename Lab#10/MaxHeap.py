from AbstractCollection import AbstractCollection
from Array import Array

class MaxHeap(AbstractCollection):
    """ A heap is a tree-based data structure that satisfies the heap property:
        The value of a node is greater than or equal to the value of its parent,
        with the minimum-value element at the root. """

    DEFAULT_CAPACITY = 10

    def __init__(self, source_collection=None):
        """ Sets the initial state of self, which includes the contents of source_collection """
        self._heap = Array(MaxHeap.DEFAULT_CAPACITY)
        AbstractCollection.__init__(self, source_collection)

    def peek(self):
        """ Return the value at the root """
        if self.is_empty():
            raise IndexError("Heap is empty!")
        return self._heap[0]

    def add(self, item):
        """ Adds 'item' to the MaxHeap, finding its correct location """

        # Begin by placing the new item in the first empty index
        self._heap[len(self)] = item
        cur_index = len(self)

        while cur_index > 0:
            # Find the parent of the current index of the new item
            parent_index = (cur_index - 1) // 2
            parent_item = self._heap[parent_index]
            if parent_item >= item:
                # Parent is greater than the new item (or equal): new item is in correct index
                break
            # Swap the parent and the child
            self._heap[cur_index] = parent_item
            self._heap[parent_index] = item
            cur_index = parent_index

        self._size += 1

    def pop(self):
        """ Remove the item at the root and reheapify the remaining items """
        if self.is_empty():
            raise IndexError("Heap is empty!")
        top_item = self._heap[0]
        bottom_item = self._heap[self._size - 1]

        self._heap[0] = bottom_item

        last_valid_index = self._size - 2

        cur_index = 0

        # In a loop, move the original final leaf (now at the root) down to its correct location
        while True:
            left_child_index = 2 * cur_index + 1
            right_child_index = 2 * cur_index + 2
            if left_child_index > last_valid_index:
                # We have no left child, therefore we have no right child. We're done
                break

            if right_child_index > last_valid_index:
                # We just have a left child, so it is the smallest
                max_child_index = left_child_index

            else:
                # We have both children, so find the smallest
                left_child = self._heap[left_child_index]
                right_child = self._heap[right_child_index]
                if left_child > right_child:
                    max_child_index = left_child_index
                else:
                    max_child_index = right_child_index

            # Compare the parent to the smallest child
            max_child = self._heap[max_child_index]
            if bottom_item >= max_child:
                # Parent is smaller than both children, so we're done
                break

            # Swap the parent and the smallest child
            self._heap[cur_index] = max_child
            self._heap[max_child_index] = bottom_item
            cur_index = max_child_index

        self._size -= 1
        return top_item