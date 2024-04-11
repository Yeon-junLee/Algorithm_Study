import sys
from collections import deque

N = int(sys.stdin.readline())
meeting = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
meet = sorted(meeting, key = lambda x : (x[1], x[0]), reverse=False)
print(meet)
result = deque()

while meet:
    if not result:
        result.append(meet[0])
        meet.pop(0)
    else:
        if result[-1][1] > meet[0][0]:
            meet.pop(0)
        else:
            result.append(meet[0])
            meet.pop(0)
print(len(result))