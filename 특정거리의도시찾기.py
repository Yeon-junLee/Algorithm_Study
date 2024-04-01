import sys
import heapq

def dijkstra(start):
    hq = []
    heapq.heappush(hq, [0, start])
    dist[start] = 0
    while hq:
        cur = hq[0][1]
        cost = hq[0][0]
        heapq.heappop(hq)
        for next in edge[cur]:
            ncost = 1
            if dist[next] > cost + ncost:
                dist[next] = cost + ncost
                heapq.heappush(hq, [dist[next], next])

N, M, K, X = map(int, sys.stdin.readline().split())
edge = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    edge[a].append(b)
dist = [999999999 for _ in range(N + 1)]
answer = []

dijkstra(X)
for i in range(1, N + 1):
    if dist[i] == K:
        answer.append(i)
answer.sort()
if answer:
    for a in answer:
        print(a)
else:
    print(-1)