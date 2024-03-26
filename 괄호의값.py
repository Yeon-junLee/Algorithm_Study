import sys
N = sys.stdin.readline()
stack = []

ans = 0 

for i in range(len(N)):
    if N[i] == '(':
        stack.append(N[i])
    elif N[i] == '[':
        stack.append(N[i])
    elif N[i] == ')':
        a
    elif N[i] == ']':
        a