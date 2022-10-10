'''
Ryo Fujimura
Exam #1
CIS 275C
'''

from LinkedList import LinkedList

def main():
    # Create a LinkedList
    list1 = LinkedList()
    list1.add_to_front(5)
    list1.add_to_front(3)
    list1.add_to_front(7)
    print(list1)

    # Create a second LinkedList
    list2 = LinkedList()
    list2.add_to_front(4)
    list2.add_to_front(2)
    list2.add_to_front(1)
    print(list2)

    # Add the two LinkedLists together
    list3 = list1 + list2
    print(list3)

    # Remove the first item from the third list
    list3.remove_from_front()
    print(list3)

    # Print the length of the third list
    print(len(list3))

if __name__ == '__main__':
    main()

'''
output:
7 3 5 
1 2 4 
7 3 5 1 2 4 
3 5 1 2 4 
5
'''