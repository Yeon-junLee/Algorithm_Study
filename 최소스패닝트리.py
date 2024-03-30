import sys
import heapq

def Prim(V):
    global ans
    hq = []
    heapq.heappush(hq, (0, 1))  ### 시작점을 1로 잡음 (cost = 0, node = 1)
    
    for i in range(V):
        while hq:
            cur = hq[0][1]
            cost = hq[0][0]
            heapq.heappop(hq)
            if visited[cur] == False:
                visited[cur] = True
                ans += cost
                break     
        for e in edge[cur]:
            heapq.heappush(hq, (e[1], e[0]))
            
V, E = map(int, sys.stdin.readline().split())
edge = [[] for _ in range(V + 1)]
for i in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    edge[a].append([b, c])
    edge[b].append([a, c])
visited = [False for _ in range(V + 1)]
ans = 0
Prim(V)

print(ans)