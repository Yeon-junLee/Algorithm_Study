import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
indegree = [0 for _ in range(N + 1)]
edge = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    edge[a].append(b)
    indegree[b] += 1

result = []
queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    cur = queue.popleft()
    result.append(cur)

    for next in edge[cur]:
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)

for res in result:
    print(res, end= " ")