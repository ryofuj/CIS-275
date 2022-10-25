# from Array import Array
# from Array import ArraySet
# from Node import Node
# from Node import LinkedSet

class AbstractSet:
    """ A superclass for both ArraySet and LinkedSet"""
    def __init__(self, source_collection=None):
        """ Initialize the set to the empty set """
        self._size = 0
        if source_collection:
            for item in source_collection:
                self.add(item)

    def add_all(self, other):
        """ Adds all items in other to self """
        for item in other:
            self.add(item)

    def remove_all(self, other):
        """ Removes all items in other from self """
        for item in other:
            self.remove(item)

    def __iter__(self):
        """ Supports iteration over a view of self """
        cursor = self._items
        while cursor != None:
            yield cursor.data
            cursor = cursor.next

    def __str__(self):
        """ Returns the string representation of the set """
        return "{" + ", ".join(map(str, self)) + "}"

    def __contains__(self, item):
        """ Returns True if item is in self, or False otherwise """
        return self.find_position(item) is not None

    def is_empty(self):
        """ Returns True if len(self) == 0, or False otherwise """
        return len(self) == 0

    def __len__(self):
        """ Returns the number of items in the set """
        return self._size

    '''
    intersection. The intersection of two sets creates a new set containing all the elements that exist in both sets. For example, if Set1 contains (1, 3, 5) and Set2 contains (1, 5, 9), the intersection of Set1 and Set2 is (1, 5). Your intersection function should take a second Set as an argument. This function should create a new Set object (either LinkedSet or ArraySet, same as the calling object), fill it with the required elements, and return it.
    '''
    def intersection(self, other):
        """ Returns a new set that is the intersection of self and other """
        result = type(self)()
        for item in self:
            if item in other:
                result.add(item)
        return result

    '''
    union. The union of two sets creates a new set containing all elements in the first set and all elements in the second set. For example, if Set1 contains (1, 3, 5) and Set2 contains (1, 5, 9), the union of Set1 and Set2 is (1, 3, 5, 9). Recall that sets do not include duplicate entries, so the union does not include 1 twice or 5 twice. Your union function should take a second Set as an argument. This function should create a new Set object, fill it with the required elements, and return it. 
    '''
    def union(self, other):
        """ Returns a new set that is the union of self and other """
        result = type(self)(self)
        result.add_all(other)
        return result