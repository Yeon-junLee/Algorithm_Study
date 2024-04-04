import sys
import heapq

def dijkstra(start):
    dist[start][start] = 0
    hq = []
    heapq.heappush(hq, (0, start))
    while hq:
        cost, cur = heapq.heappop(hq)
        for next in edge[cur]:
            if dist[start][next] > cost + 1:
                dist[start][next] = cost + 1
                heapq.heappush(hq, (dist[start][next], next))


N, M = map(int, sys.stdin.readline().split())
edge = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    edge[a].append(b)
    # edge[b].append(a)
INF = 99999999999
dist = [[INF for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    dijkstra(i)

ans = 0
ansli = []
# j번 column에서 INF, 0 이 아닌 요소들의 개수 > N / 2 면 절반 제외
for j in range(1, N + 1):
    num = 0
    for i in range(1, N + 1):
        if dist[i][j] > 0 and dist[i][j] != INF:
            num += 1
        if num > N / 2:
            break
    if num > N / 2:
        ansli.append(j)
        ans += 1
# i번 row에서 INF, 0 아닌 요소들의 개수 > N / 2 면 절반 제외
for i in range(1, N + 1):
    num2 = 0
    for j in range(1, N + 1):
        if dist[i][j] > 0 and dist[i][j] != INF:
            num2 += 1
        if num2 > N / 2:
            break
    if num2 > N / 2 and i not in ansli:
        ansli.append(i)
        ans += 1


print(ans)