from AbstractCollection import AbstractCollection
from Array import Array

class MaxHeap(AbstractCollection):
   """ An array-based max-heap implementation """

   DEFAULT_CAPACITY = 10

   def __init__(self):
      self._heap = Array(MaxHeap.DEFAULT_CAPACITY)
      AbstractCollection.__init__(self)

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

      self._numitems += 1

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
            # We just have a left child, so it is the largest
            max_child_index = left_child_index

         else:
            # We have two children, check to see which is larger
            left_child = self._heap[left_child_index]
            right_child = self._heap[right_child_index]

            if left_child > right_child:
               max_child_index = left_child_index
            else:
               max_child_index = right_child_index

         max_child = self._heap[max_child_index]

         if bottom_item >= max_child:
            # Item being moved is greater than both children. Stop here
            break

         # Item being moved is smaller than its max child. Swap and continue
         self._heap[cur_index] = max_child
         self._heap[max_child_index] = bottom_item
         cur_index = max_child_index

      self._numitems -= 1
      return top_item

   def __iter__(self):
      """ Iterate over the items in the heap """
      for i in range(self._size):
         yield self._heap[i]

   def __str__(self):
      """ Return a string representation of the heap """
      return str(self._heap)

   def __len__(self):
      """ Return the number of items in the heap """
      return self._numitems

   def __eq__(self, other):
      """ Return True if the heap is equal to the other heap """
      if self is other: return True
      if type(self) != type(other): return False
      if len(self) != len(other): return False
      for i in range(len(self)):
         if self._heap[i] != other._heap[i]:
            return False
      return True

   def __ne__(self, other):
      """ Return True if the heap is not equal to the other heap """
      return not self.__eq__(other)

   def __lt__(self, other):
      """ Return True if the heap is less than the other heap """
      if self is other: return False
      if type(self) != type(other): return False
      if len(self) != len(other): return False
      for i in range(len(self)):
         if self._heap[i] < other._heap[i]:
            return True
         elif self._heap[i] > other._heap[i]:
            return False
      return False

   def __le__(self, other):
      """ Return True if the heap is less than or equal to the other heap """
      return self.__lt__(other) or self.__eq__(other)

   def __gt__(self, other):
      """ Return True if the heap is greater than the other heap """
      return not self.__le__(other)

   def __ge__(self, other):
      """ Return True if the heap is greater than or equal to the other heap """
      return not self.__lt__(other)