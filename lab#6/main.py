'''
Ryo Fujimura
Lab Assignment #6
CIS 275C
'''

from LinkedStack import LinkedStack

class InfixToPostfix:
    def __init__(self):
        """constructor"""
        self._string = ""
        self._postfix = ""
        self._result = 0

    def precedence(ch):
        """return the precedence of the operator"""
        if ch == '*' or ch == '/':
            return 2
        elif ch == '+' or ch == '-':
            return 1
        else:
            return 0

    def is_balanced(string):
        """check if the string is balanced"""
        s = LinkedStack()
        for ch in string:
            if ch in ['(', '{', '[']:
                s.push(ch)
            elif ch in ['}']:
                if s.is_empty() or s.pop() != '{':
                    return False
                else:
                    s.pop()
            elif ch in [']']:
                if s.is_empty() or s.pop() != '[':
                    return False
                else:
                    s.pop()
            elif ch in [')']:
                if s.is_empty() or s.pop() != '(':
                    return False
                else:
                    s.pop()
        return s.is_empty()

    def convertToPostfix(string):
        """convert the infix expression to postfix expression"""
        stack = LinkedStack()
        postfix = ""
        for ch in string:
            if ch == '(':
                stack.push(ch)
            elif ch == ')':
                while not stack.is_empty() and stack.peek() != '(':
                    postfix += stack.pop()
                stack.pop()
            elif ch in "*/+-":
                while not stack.is_empty() and stack.peek() != '(' and InfixToPostfix.precedence(ch) <= InfixToPostfix.precedence(stack.peek()):
                    postfix += stack.pop()
                stack.push(ch)
            else:
                postfix += ch
        while not stack.is_empty():
            postfix += stack.pop()

        return postfix

    def evaluatePostfix(string):
        """evaluate the postfix expression"""
        stack = LinkedStack()
        for ch in string:
            if ch in "0123456789":
                stack.push(int(ch))
            else:
                if ch == '+':
                    stack.push(stack.pop() + stack.pop())
                elif ch == '-':
                    stack.push(-stack.pop() + stack.pop())
                elif ch == '*':
                    stack.push(stack.pop() * stack.pop())
                elif ch == '/':
                    stack.push(1 / stack.pop() * stack.pop())
        return stack.pop()

if __name__ == "__main__":
    string = input("Enter an infix expression: ")
    if InfixToPostfix.is_balanced(string):
        print("Postfix expression: ", InfixToPostfix.convertToPostfix(string))
        print("Result: ", InfixToPostfix.evaluatePostfix(InfixToPostfix.convertToPostfix(string)))
    else:
        print("The infix expression is not balanced")