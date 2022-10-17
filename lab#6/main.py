'''
Ryo Fujimura
Lab Assignment #6
CIS 275C
driver file
'''
from InfixToPostfix import InfixToPostfix

def main():
    while True:
        print("Enter an infix expression ('q' to quit):")
        string = input()
        if string == 'q':
            break
        if InfixToPostfix.is_balanced(string):
            print("Postfix form: " + InfixToPostfix.convertToPostfix(string))
        else:
            print("The expression is not balanced.")

if __name__ == "__main__":
    main()
    