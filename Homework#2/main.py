'''
For this assignment, you will write a program to allow the user to store the names and phone numbers of their contacts. Create the following classes:

    Contact: two attributes. One for the contact's name and the contact's phone number.
    Node: two attributes: _data and _next. For use in a linked list.
    ContactList: One attribute: _head, a reference to the head of an internal linked list of Node objects.
    Note: self._head is an attribute of the class, so any method which updates the internal linked list can simply update the list self._head references. There is no need to return anything like we did in methods such as add_to_end in the lecture. Note also that for the same reason, we do not have to pass a reference to the head of the list to any method, because each method should already have access to the self._head attribute.

 '''

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
            
    def __str__(self):
        return self.name + ": " + self.phone + "\n"

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

'''
ContactList should also have the following methods:

    add(name, new_number). Creates a new Node with a Contact object as its _data. The new Node is then added to ContactList's internal linked list referenced by _first_node. This will be a little different from what we've seen so far, because the Contacts should remain sorted in alphabetical order. When a Node is added to the linked list, find its correct location based on the Contact it holds and place the Node there. Do not worry about sorting by last name, just by overall name i.e., "Ryan Adams" should go after "Jill Smith". String objects in Python can be tested for alphabetical ordering with the > and < operators.
    Override __str__ so that it returns a nicely formatted string with each Contact's name and phone number.
    remove(name). Remove the Contact with the given name from the list, if it exists.
    change_phone_number(name, new_number). Update the phone number of the contact with the given name, if it exists. 
'''

class ContactList:
    def __init__(self):
        self._head = None

    def add(self, name, new_number):
        contact = Contact(name, new_number)
        node = Node(contact)
        if self._head == None:
            self._head = node
        elif self._head.data.name > contact.name:
            node.next = self._head
            self._head = node
        else:
            current = self._head
            while current.next != None and current.next.data.name < contact.name:
                current = current.next
            node.next = current.next
            current.next = node

    def __str__(self):
        current = self._head
        string = ""
        while current != None:
            string += str(current.data) + ""
            current = current.next
        return string

    def remove(self, name):
        current = self._head
        previous = None
        while current != None and current.data.name != name:
            previous = current
            current = current.next
        if current == None:
            print("Name does not exist, invalid input")
        elif previous == None:
            self._head = current.next
        else:
            previous.next = current.next

    def change_phone_number(self, name, new_number):
        current = self._head
        while current != None and current.data.name != name:
            current = current.next
        if current == None:
            print("Name does not exist, invalid input")
        else:
            current.data.phone = new_number
        


'''
On main.py, create a ContactList object and then write a menu-based while loop that gives the user five options: add, remove, change phone number, print contacts, and quit. Make sure to test as many corner cases as possible (i.e., does it work when you remove the first Contact? How about the last Contact? etc.)

    Note:  You are not required to perform a sort on the list!
    When you add a new Contact, the method only needs to find the correct location for that particular object.
    For example, if the user adds 'Bob' to an empty ContactList, it becomes the first (and only) Contact.
    If the user then adds 'Adam', it becomes the new head of the list (since it comes before 'Bob' alphabetically).
    Finally, if the user adds Barb, the list should be Adam ->Barb ->Bob.
    Hint: each call to 'add' only adds a single Contact to a list which is already in sorted order.
'''

def main():
    contacts = ContactList()
    while True:
        print("1. Add")
        print("2. Remove")
        print("3. Change phone number")
        print("4. Print contacts")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter name: ")
            number = input("Enter number: ")
            contacts.add(name, number)
        elif choice == "2":
            name = input("Enter name: ")
            contacts.remove(name)
        elif choice == "3":
            name = input("Enter name: ")
            number = input("Enter number: ")
            contacts.change_phone_number(name, number)
        elif choice == "4":
            print(contacts)
        elif choice == "5":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()