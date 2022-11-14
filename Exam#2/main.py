'''
Ryo Fujimura
CIS275C
Exam #2
'''
from ArrayStack import ArrayStack

def main():
    # Create a stack to store the history of calculations
    undo_stack = ArrayStack()
    redo_stack = ArrayStack()
    # Initialize the current value to 0
    current_value = 0
    # Loop until the user quits
    while True:
        # Ask the user to select an option
        # Print the current value
        print("\nCurrent value: " + str(current_value))
        user_input = input("Enter a number, 'u' to undo, 'r' to redo, 'q' to quit: ")
        # If the user entered a number, perform the calculation
        if user_input.isdigit():
            # Ask the user for the operator
            operator = input("Enter an operator: ")
            # Perform the calculation
            if operator == "+":
                print(str(current_value) + " + " + user_input + " = " + str(current_value + int(user_input)))
                result = current_value + int(user_input)
            elif operator == "-":
                print(str(current_value) + " - " + user_input + " = " + str(current_value - int(user_input)))
                result = current_value - int(user_input)
            elif operator == "*":
                print(str(current_value) + " * " + user_input + " = " + str(current_value * int(user_input)))
                result = current_value * int(user_input)
            elif operator == "/":
                print(str(current_value) + " / " + user_input + " = " + str(current_value / int(user_input)))
                result = current_value / int(user_input)
            else:
                print("Invalid operator")
                continue
        
            # Push the current value onto the undo stack
            undo_stack.push(current_value)
            # Clear the redo stack
            redo_stack.clear()
            # Set the current value to the result
            current_value = result
        # If the user entered 'u', undo the last calculation
        elif user_input == "u":
            # If the undo stack is empty, inform the user
            if undo_stack.is_empty():
                print("No more actions to undo!")
            else:
                # Push the current value onto the redo stack
                redo_stack.push(current_value)
                # Pop the last value off the undo stack
                current_value = undo_stack.pop()
        # If the user entered 'r', redo the last undo
        elif user_input == "r":
            # If the redo stack is empty, inform the user
            if redo_stack.is_empty():
                print("No more actions to redo!")
            else:
                # Push the current value onto the undo stack
                undo_stack.push(current_value)
                # Pop the last value off the redo stack
                current_value = redo_stack.pop()
        # If the user entered 'q', quit the program
        elif user_input == "q":
            break
        # If the user entered an invalid option, inform them
        else:
            print("Invalid option")


if __name__ == "__main__":

    main()

