from AbstractCollection import AbstractCollection
from Node import Node


class LinkedQueue(AbstractCollection):
	def __init__(self):
		self._front = None
		self._rear = None
		AbstractCollection.__init__(self)

	def add(self, new_item):
		""" Add a new item to the back of the queue """
		new_node = Node(new_item)
		if self.is_empty():
			# Queue is empty. New item is both the front and back of queue
			self._front = new_node
			self._rear = new_node
		else:
			# Queue is not empty. Point the last node (and tail pointer) to it
			self._rear.next = new_node
			self._rear = self._rear.next

		self._size += 1

	def pop(self):
		""" Removes and returns the item at front of the queue
		Precondition: Queue is not empty
		Raises: ValueError if Queue is empty
		Postcondition: Queue has one less item in it (front item removed)
		:return: The item that was removed
		"""

		if self.is_empty():
			raise ValueError("Queue is empty!")

		return_item = self._front.data
		self._front = self._front.next

		# If queue is now empty, update rear as well
		if self._front is None:
			self._rear = None

		self._size -= 1
		return return_item

	def clear(self):
		""" Makes queue empty """
		self._front = None
		self._rear = None
		self._size = 0

	def peek(self):
		"""
		Returns entry at front of queue
		Precondition: Queue is not empty
		Raises: ValueError if queue is empty
		"""

		if self.is_empty():
			raise ValueError("Queue is empty!")
		return self._front.data

	def print_queue(self):
		probe = self._front
		while probe:
			print(probe.data, end=" ")
			probe = probe.next
