# Problem Description
# Given a string A consisting only of '(' and ')'.
# You need to find whether parantheses in A is balanced or not ,if it is balanced then return 1 else return 0.
from collections import deque

def solve(A):
    stack = deque()
    if not A:
        return 1

    for i in range(len(A)):
        if A[i] == '(':
            stack.append(A[i])
        if stack and (A[i] == ')') and (stack[-1] == '('):
            stack.pop()
        # else:
        #     stack.append(A[i])
        print(stack)
    if stack:
        return 0
    return 1


print(solve("(()())"))
