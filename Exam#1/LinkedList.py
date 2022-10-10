'''
Ryo Fujimura
Exam #1
CIS 275C
'''

from Node import Node

class LinkedList:
	def __init__(self):
		self._head = None

	def __len__(self):
		""" Return the number of Nodes in the list """
		count = 0
		probe = self._head
		while probe is not None:
			count += 1
			probe = probe.next
		return count

	def __eq__(self, other):
		if type(self) != type(other):
			return False
		if len(self) != len(other):
			return False
		probe1 = self._head
		probe2 = other._head
		while probe1 is not None:
			if probe1.data != probe2.data:
				return False
			probe1 = probe1.next
			probe2 = probe2.next
		return True

	def add_to_front(self, data):
		""" Add a new Node to the front of the LinkedList, with 'data' as its data attribute """
		self._head = Node(data, self._head)

	def add_to_back(self, data):
		""" Add a new Node to the back of the LinkedList, with 'data' as its data attribute """
		if self._head is None:
			self._head = Node(data)
		else:
			probe = self._head
			while probe.next is not None:
				probe = probe.next
			probe.next = Node(data)

	def __add__(self, other):
		""" Return a new LinkedList which contains the data of the left operand followed by the data of the right operand """
		new_list = LinkedList()
		probe = self._head
		while probe is not None:
			new_list.add_to_back(probe.data)
			probe = probe.next
		probe = other._head
		while probe is not None:
			new_list.add_to_back(probe.data)
			probe = probe.next
		return new_list

	def remove_from_front(self):
		""" Remove the Node at the front of the list """
		self._head = self._head.next

	def __str__(self):
		""" Return a string representation of the list """
		s = ""
		probe = self._head
		while probe is not None:
			s += str(probe.data) + " "
			probe = probe.next
		return s

	def print_list(self):
		""" Print all the data in this linked list """
		probe = self._head
		while probe is not None:
			print(probe.data, end=" ")
			probe = probe.next
