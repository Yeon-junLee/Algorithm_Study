import sys
from queue import PriorityQueue

N = int(sys.stdin.readline())

maxpq = PriorityQueue()
minpq = PriorityQueue()
mid = 0
ans = []
for i in range(N):
    num = int(sys.stdin.readline())
    if i == 0:
        # 첫번째는 무조건 가운데 값
        mid = num
    else:
        if num >= mid:
            # 현재 mid와 비교해서 더 크면 minheap(min priority queue)에
            minpq.put(num)
        else:
            # 현재 mid와 비교해서 더 작으면 maxheap(max priority queue)에
            maxpq.put(-num)
    minsize = minpq.qsize()
    maxsize = maxpq.qsize()
    if minsize > maxsize and minsize - maxsize > 1:
        # min heap과 max heap의 크기를 비교해서 min heap의 크기가 더 크면 min heap에서 하나 빼서 mid, 원래 mid는 max heap으로
        # 크기 차이가 1 까지는 괜찮은 이유는 만약 중간 인덱스가 두 개 라면 더 작은 것을 출력하기 때문
        newmid = minpq.get()
        maxpq.put(-mid)
        mid = newmid
    elif maxsize > minsize:
        # min heap과 max heap의 크기를 비교해서 max heap의 크기가 더 크면 max heap에서 하나 빼서 mid, 원래 mid는 min heap으로
        newmid = -maxpq.get()
        minpq.put(mid)
        mid = newmid
    print(mid)