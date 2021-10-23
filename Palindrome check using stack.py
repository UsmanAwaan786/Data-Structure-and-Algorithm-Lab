from collections import deque

reverse_string = ''
stack3 = deque()  # create stack
string = input("enter the string: ")  # take input
for i in range(len(string)):
    stack3.append(string[i])  # append the input one by one in stack

while not (len(stack3) == 0):
    reverse_string += stack3.pop()  # pop the output one by one and store in a variable until stack is empty

if reverse_string == string:  # compare the original sting with reversed  string
    print("entered string is palindrome")  # print the output
else:
    print("entered string is not palindrome")
