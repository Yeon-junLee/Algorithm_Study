import sys
from queue import PriorityQueue

N = int(sys.stdin.readline())
pq = PriorityQueue()

for i in range(N):
    order = int(sys.stdin.readline())
    if order == 0:
        if pq.empty():
            print(0)
        else:
            print(pq.get()[1])
    else:
        pq.put((-order, order))