import sys
N = int(sys.stdin.readline())
order = [list(sys.stdin.readline().split()) for _ in range(N)]

for i in range(N):
    if len(order[i]) > 1:
        order[i][1] = int(order[i][1])

stack = []

for i in range(N):
    if order[i][0] == 'push':
        stack.append(order[i][1])
    elif order[i][0] == 'pop':
        if len(stack) > 0:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
    elif order[i][0] == 'size':
        print(len(stack))
    elif order[i][0] == 'empty':
        if len(stack):
            print(0)
        else:
            print(1)
    elif order[i][0] == 'top':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
    else:
        print("오류 발생!")
        break