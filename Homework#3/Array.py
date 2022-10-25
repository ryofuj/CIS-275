class Array:

    def __init__(self, capacity, fill_value=None):
        """ Capacity is the static size of the array
            Each index in the array is filled with fill_value """
        self._items = []
        for count in range(capacity):
            self._items.append(fill_value)

    def __len__(self):
        """ Returns the length of this array """
        return len(self._items)

    def __str__(self):
        """ Returns a string representation of this array """
        return str(self._items)

    def __iter__(self):
        """ Supports iteration with a for loop """
        return iter(self._items)

    def __getitem__(self, index):
        """ Retrieves the item at 'index' """
        return self._items[index]

    def __setitem__(self, index, new_item):
        """ Sets the internal list's index to 'new_item' """
        self._items[index] = new_item

class ArraySet:
    """Implements a set using an Array to store its internal data"""
    def __init__(self, source_collection=None):
        """Initializes the set to contain the items in source_collection, if it's present"""
        self._items = Array(7)
        self._size = 0
        if source_collection:
            for item in source_collection:
                self.add(item)

    def __iter__(self):
        """Supports iteration over a view of self"""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def __str__(self):
        """Returns the string representation of the set"""
        return "{" + ", ".join(map(str, self)) + "}"

    def __len__(self):
        """Returns the number of items in the set"""
        return self._size

    def __contains__(self, item):
        """Returns True if item is in self, or False otherwise"""
        return item in self._items

    def add(self, item):
        """Adds item to self"""
        if item not in self:
            self._items[self._size] = item
            self._size += 1

    def remove(self, item):
        """Precondition: item is in self
        Raises: KeyError if item is not in self
        Postcondition: item is removed from self"""
        if item not in self:
            raise KeyError(str(item) + " not in set")
        # Find index of target item
        target_index = 0
        for target_item in self:
            if target_item == item:
                break
            target_index += 1
        # Shift items to the left of target up by one position
        for i in range(target_index, len(self) - 1):
            self._items[i] = self._items[i + 1]
        # Decrement logical size
        self._size -= 1

    def is_empty(self):
        """Returns True if len(self) == 0, or False otherwise"""
        return len(self) == 0

    def clear(self):
        """Makes self become empty"""
        self._size = 0

    def __eq__(self, other):
        """Returns True if self equals other, or False otherwise"""
        if self is other: return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        for item in self:
            if item not in other:
                return False

        return True

    def __add__(self, other):
        """Returns a new set containing the contents of self and other"""
        result = ArraySet(self)
        result += other
        return result