import sys

def bfs(x, y):
    global ans
    visited[x][y] = True
    queue = []
    queue.append([x, y])
    num = []
    num.append(1)
    while queue:
        cx = queue[0][0]
        cy = queue[0][1]
        cn = num[0]
        queue.pop(0)
        num.pop(0)

        if cx == N - 1 and cy == M - 1:
            ans = cn
            break

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == False:
                    if graph[nx][ny] == '1':
                        queue.append([nx, ny])
                        visited[nx][ny] = True
                        num.append(cn + 1)
                


N, M = map(int, sys.stdin.readline().split())
graph = [list(str(sys.stdin.readline().strip())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = 999999999999
bfs(0, 0)
print(ans)