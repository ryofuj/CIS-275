'''
    A set is an unordered collection which is similar to a bag except it cannot contain duplicate entries. If the client tries to add a duplicate entry to a set, the item is ignored. 
    Create the following classes:
        AbstractSet: A superclass for both ArraySet and LinkedSet.
        ArraySet: Implements a set using an Array to store its internal data. Use thisDownload this Array class
        LinkedSet: Implements a set using a Linked List to store its internal data. Use thisDownload this Node class. 
    Implement add, remove, __iter__, __str__, __contains__, is_empty, and __len__ for both, either in each class individually or in AbstractSet.
    Your two set classes should also include the following two functions. You may define these functions either in AbstractSet or once in ArraySet and once in LinkedSet :
        intersection. The intersection of two sets creates a new set containing all the elements that exist in both sets. For example, if Set1 contains (1, 3, 5) and Set2 contains (1, 5, 9), the intersection of Set1 and Set2 is (1, 5). Your intersection function should take a second Set as an argument. This function should create a new Set object (either LinkedSet or ArraySet, same as the calling object), fill it with the required elements, and return it.
        union. The union of two sets creates a new set containing all elements in the first set and all elements in the second set. For example, if Set1 contains (1, 3, 5) and Set2 contains (1, 5, 9), the union of Set1 and Set2 is (1, 3, 5, 9). Recall that sets do not include duplicate entries, so the union does not include 1 twice or 5 twice. Your union function should take a second Set as an argument. This function should create a new Set object, fill it with the required elements, and return it. 
    Utilize inheritance as much as possible (i.e., place as much in AbstractSet as you can). Points may be taken off if AbstractSet is too short!
'''
