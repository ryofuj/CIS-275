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

	def print_list(self):
		""" Print all the data in this linked list """
		probe = self._head
		while probe is not None:
			print(probe.data, end=" ")
			probe = probe.next
