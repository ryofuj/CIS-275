'''
Ryo Fujimura
Lab Assignment #6
CIS 275C
'''
from InfixToPostfix import InfixToPostfix

def main():
    string = input("Enter an infix expression: ")
    if InfixToPostfix.is_balanced(string):
        print("Postfix expression: ", InfixToPostfix.convertToPostfix(string))
        print("Result: ", InfixToPostfix.evaluatePostfix(InfixToPostfix.convertToPostfix(string)))
    else:
        print("The infix expression is not balanced")

if __name__ == "__main__":
    main()
    