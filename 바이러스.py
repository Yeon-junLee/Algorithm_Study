import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

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
    num = 0
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

print(bfs(1))