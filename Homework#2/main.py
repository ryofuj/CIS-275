'''
Ryo Fujimura
Homework #2
CIS-275
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
            print("Name does not exist.")
        elif previous == None:
            self._head = current.next
        else:
            previous.next = current.next

    def change_phone_number(self, name):
        current = self._head
        while current != None and current.data.name != name:
            current = current.next
        if current == None:
            print("Name does not exist.")
        else:
            new_number = input("Enter number: ")
            current.data.phone = new_number
        

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
            # number = input("Enter number: ")
            # contacts.change_phone_number(name, number)
            contacts.change_phone_number(name)
        elif choice == "4":
            print(contacts)
        elif choice == "5":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
