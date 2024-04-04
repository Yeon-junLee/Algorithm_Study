import sys
import heapq

N = int(sys.stdin.readline())
outdegree = [0 for _ in range(N + 1)]
edge = [[] for _ in range(N + 1)]

for i in range(N):
    string = str(sys.stdin.readline().strip())
    for j in range(N):
        if string[j] =='1':
            edge[j + 1].append(i + 1)
            outdegree[i + 1] += 1
hq = []
visited = [False for _ in range(N + 1)]
visited[0] = True
## 역 위상정렬이 필요함
## outdegree가 0 인것들을 maxheap에 넣어 큰 노드부터 나오게 해서 숫자 부여
## outdegree 감소시키면서 넣는 것은 원래 위상정렬과 동일

for i in range(1, N + 1):
    if outdegree[i] == 0:
        heapq.heappush(hq, -i)

answer = [0 for _ in range(N)]
number = N
while hq:
    cur = -heapq.heappop(hq)
    visited[cur] = True
    answer[cur - 1] = number
    number -= 1
    for next in edge[cur]:
        outdegree[next] -= 1
        if outdegree[next] == 0:
            heapq.heappush(hq, -next)
if False in visited:
    print(-1)
else:
    for a in answer:
        print(a, end=" ")