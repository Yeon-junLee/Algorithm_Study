import sys

N = int(sys.stdin.readline())

edge = [[] for _ in range(N + 1)]

for i in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    edge[a].append(b)
    edge[b].append(a)

visited = [False for _ in range(N + 1)]
visited[1] = True
parent = [0 for _ in range(N + 1)]

def bfs(root):
    queue = []
    queue.append(root)
    while queue:
        cur = queue[0]
        queue.pop(0)
        for next in edge[cur]:
            if visited[next]:
                continue
            else:
                parent[next] = cur
                visited[next] = True
                queue.append(next)
bfs(1)
for i in range(2, N + 1):
    print(parent[i])