import sys
import heapq

def dijkstra(node):
    hq = []
    dist[node] = 0
    heapq.heappush(hq, [0, node])
    while hq:
        cur = hq[0][1]
        cost = hq[0][0]
        heapq.heappop(hq)

        if cost > dist[cur]:
            continue
        for line in edge[cur]:
            next = line[0]
            ncost = line[1]

            if dist[next] > cost + ncost:
                dist[next] = cost + ncost
                heapq.heappush(hq, [cost + ncost, next])

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
edge = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    edge[a].append([b, c])
start, end = map(int, sys.stdin.readline().split())

dist = [9999999999 for _ in range(N + 1)]
dijkstra(start)
print(dist[end])