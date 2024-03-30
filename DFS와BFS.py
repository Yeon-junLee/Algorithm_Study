import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
edge = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    edge[a].append(b)
    edge[b].append(a)
visited1 = [False for _ in range(N + 1)]
visited2 = [False for _ in range(N + 1)]
for i in edge:
    i.sort()

def dfs(start):
    print(start,end=" ")
    visited1[start] = True
    for n in edge[start]:
        if visited1[n] is False:
            visited1[n]= True
            dfs(n)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited2[start] = True
    while queue:
        cur = queue[0]
        queue.popleft()
        print(cur, end=" ")
        for next in edge[cur]:
            if visited2[next] is False:
                queue.append(next)
                visited2[next] = True
dfs(V)
print()
bfs(V)