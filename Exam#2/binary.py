'''
Ryo Fujimura
CIS275C
Exam #2
ec
'''

from ArrayStack import ArrayStack

def main():
    # Create a stack
    stack = ArrayStack()
    while True:
        # Ask the user for a binary string
        binary_string = input("\nEnter a binary string ('q' to quit): ")
        # If the user entered 'q', quit the program
        if binary_string == "q":
            break
        # Iterate through the string
        for char in binary_string:
            # If the character is not a 1 or 0, inform the user and exit
            if char != "1" and char != "0":
                print("Invalid binary string!")
                result = False
                break
            # If the stack is empty, push the character onto the stack
            if stack.is_empty():
                stack.push(char)
                result = True
            # If the character is the not same as the top of the stack, pop it off
            elif char != stack.peek():
                stack.pop()
            # Otherwise, push the character onto the stack
            else:
                stack.push(char)
        if result == True:
            # If the stack is empty, inform the user that the string contains the same number of 0s and 1s
            if stack.is_empty():
                print("Same number of 0s and 1s")
            # Otherwise, inform the user that the string does not contain the same number of 0s and 1s
            else:
                print("Not same number of 0s and 1s")
            
        # Clear the stack
        stack.clear()

if __name__ == "__main__":
    main()
