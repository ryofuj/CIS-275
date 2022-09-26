class Node:
    """ represents a singly-linked node """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
'''
In your main function, allow the user to keep adding items to a linked list until they are finished (you may copy the main function from slide 41, where names are added until the user enters 'q'). After the user is done creating the linked list, pass the head to the following functions which you will create:

    'length'. This function accepts the head of a linked list and returns the number of items in it.
    'num_times'. This function accepts the head of a linked list and a target value. It should return the number of times the target value appears in the linked list. For your test code, you may simply hardcode a value for the target.
'''

def main():
    head = None
    while True:
        name = input("Enter a name (quit:q): ")
        if name == 'q':
            break
        head = Node(name, head)
    print("Length: ", length(head))
    print("Number of times: ", num_times(head, "targetname"))

def length(head):
    count = 0
    while head != None:
        count += 1
        head = head.next
    return count

def num_times(head, target):
    count = 0
    while head != None:
        if head.data == target:
            count += 1
        head = head.next
    return count

main()

'''
Output:

Enter a name (quit:q): Q
Enter a name (quit:q): quit
Enter a name (quit:q): name
Enter a name (quit:q): targetname
Enter a name (quit:q): targetname
Enter a name (quit:q): name
Enter a name (quit:q): q
Length:  6
Number of times:  2


'''