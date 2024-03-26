from collections import deque
import sys
N = int(sys.stdin.readline())

queue = deque()

for i in range(N):
    order = sys.stdin.readline().strip()
    if 'push' in order:
        o, num = order.split()
        queue.append(num)
    elif 'pop' in order:
        if len(queue) > 0:
            print(queue.popleft())
        else:
            print(-1)
    elif 'size' in order:
        print(len(queue))
    elif 'empty' in order:
        if len(queue):
            print(0)
        else:
            print(1)
    elif 'front' in order:
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
    elif 'back' in order:
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)
    else:
        print("오류 발생!")
        break