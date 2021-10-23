from collections import deque

stack3 = deque()  # create stack


def Balanced(Expression):  # function body
    for paren in Expression:
        if paren == '(' or paren == '{' or paren == '[':  # conditions for input
            stack3.append(paren)
        if paren == ')' or paren == '}' or paren == ']':
            if len(stack3) == 0:  # condition to check empty stack
                return False
            top = stack3.pop()  # compare the parenthesis with entered parenthesis
            if (top == '(' and paren != ')') or (top == '{' and paren != '}' or (top == '[' and paren != ']')):
                return False
    return not stack3  # return the stack if it is empty


if __name__ == '__main__':  # main body
    Expression = input("enter the Expression: ")  # take input
    if Balanced(Expression):  # call function
        print("expression is balanced")  # display output
    else:
        print(" expression is  not balanced")
