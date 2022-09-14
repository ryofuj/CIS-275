"""
Ryo Fujimura
Homework#1

Add an instance variable named logical_size which tracks the array's logical size. Add a getter method to return this value to the client. Note: The len function should still return the array's physical size.

Make the following changes to __setitem__: 
    If the client tries to update an index further than the first logically empty index of the array, raise an error.
        i.e. if the array a contains [1, 2, None, None, None] and the user attempts a[3] = 10, this is an error!
    If the client tries to set an index to None, make sure it is the last logically filled index of the array.
        i.e. if an array's first 3 indexes have valid data in them, do not allow the client to say array[1] = None

Add the method __eq__ to the Array class. Python runs this method when an Array object appears as the left operand of the == operator. The method should returns True if its argument is also an Array, it has the same logical size as the calling object, and the items at each corresponding logical index in both Arrays are equal. Otherwise it should return False

"""

class Array:

	def __init__(self, capacity):
		""" Capacity is the static size of the array. Each index is initialized to None """

		self._items = []
		for i in range(capacity):
			self._items.append(None)

	def __len__(self):
		""" Returns the capacity of this Array """

		return len(self._items)

	def __str__(self):
		""" Returns a string representation of this Array """

		return str(self._items)

	def __iter__(self):
		""" Returns an iterator over the Array """

		return iter(self._items)

	def __getitem__(self, index):
		""" Return the item at the given index """

		return self._items[index]

	def __setitem__(self, index, new_item):
		""" Adds the value 'new_item' to the array at the given index """
		
		if index > self.logical_size():
			raise IndexError("Index out of range")
		elif new_item == None:
			raise ValueError("Cannot set to None")
		else:
			self._items[index] = new_item
		
	
	def logical_size(self):
		""" Returns the logical size of the array """
		'''
		logical_size = 0
				for i in range(len(self)):
					if self[i] != None:
						logical_size += 1
				return logical_size
		'''
		return len(self._items) - self._items.count(None)		
		
	def __eq__(self, other):
		""" Returns True if the two arrays are equal, False otherwise """

		if len(self) != len(other):
			return False

		for i in range(len(self)):
			if self[i] != other[i]:
				return False

		return True

