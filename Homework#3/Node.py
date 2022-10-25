class Node:
	def __init__(self, data, next=None):
		self._data = data
		self._next = next

	@property
	def next(self):
		return self._next

	@next.setter
	def next(self, val):
		self._next = val

	@property
	def data(self):
		return self._data

	@data.setter
	def data(self, data):
		self._data = data

class LinkedSet:
	"""LinkedSet: Implements a set using a Linked List to store its internal data."""
	def __init__(self, source_collection=None):
		"""Initializes the set to contain the items in source_collection, if it's present."""
		self._items = None
		self._size = 0
		if source_collection:
			for item in source_collection:
				self.add(item)

	def __iter__(self):
		"""Supports iteration over a view of self."""
		cursor = self._items
		while cursor != None:
			yield cursor.data
			cursor = cursor.next

	def __str__(self):
		"""Returns the string representation of the set."""
		return "{" + ", ".join(map(str, self)) + "}"

	def __len__(self):
		"""Returns the number of items in the set."""
		return self._size

	def __contains__(self, item):
		"""Returns True if item is in self, or False otherwise."""
		return self.find_position(item) is not None

	def add(self, item):
		"""Adds item to self."""
		if item not in self:
			self._items = Node(item, self._items)
			self._size += 1

	def remove(self, item):
		"""Precondition: item is in self.
		Raises: KeyError if item is not in self.
		Postcondition: item is removed from self."""
		# Find the node and its predecessor
		pred_node = self.find_position(item)
		# Unhook the node to be deleted, either the first one or one further down
		if pred_node is None:
			# Deleting the first node
			self._items = self._items.next
		else:
			pred_node.next = pred_node.next.next
		self._size -= 1

	def find_position(self, item):
		"""Returns the position of item in self, or None if item is not in self."""
		pred_node = None
		cursor = self._items
		while cursor != None and cursor.data != item:
			pred_node = cursor
			cursor = cursor.next
		return pred_node

	def clear(self):
		"""Makes self become empty."""
		self._size = 0
		self._items = None

	def is_subset(self, other_set):
		"""Returns True if self is a subset of other_set, or False otherwise."""
		if len(self) > len(other_set):
			return False
		for item in self:
			if item not in other_set:
				return False
		return True

	def union(self, other_set):
		"""Returns a new set that is the union of self and other_set."""
		result = LinkedSet(self)
		for item in other_set:
			result.add(item)
		return result