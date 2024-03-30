import sys

N, M = map(int, sys.stdin.readline().split())

edge = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    edge[a].append(b)
    edge[b].append(a)

visited = [False for _ in range(N + 1)]

def bfs(node):
    queue = []
    visited[node] = True
    queue.append(node)
    num = 1
    while queue:
        cur = queue[0]
        queue.pop(0)

        for next in edge[cur]:
            if visited[next]:
                continue
            else:
                visited[next] = True
                queue.append(next)
                num += 1
    return num
area = []
for i in range(1, N + 1):
    if visited[i] is False:
        area.append(bfs(i))
print(len(area))