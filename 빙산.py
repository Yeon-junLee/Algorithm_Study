import sys
from collections import deque

def bfs(x, y):
    a = 0
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        cx, cy = queue.popleft()
        a += 1
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 1 <= nx < N - 1 and 1 <= ny < M - 1:
                if visited[nx][ny] == False:
                    if arctic[nx][ny] > 0:
                        queue.append((nx, ny))
                        visited[nx][ny] = True
    return a

N, M = map(int, sys.stdin.readline().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
arctic = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
year = 0

while True:
    consea = []
    area = []
    visited=[[False for _ in range(M)] for _ in range(N)]
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if visited[i][j] == False and arctic[i][j] > 0:
                area.append(bfs(i, j))
            if arctic[i][j] > 0:
                num = 0
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if 0 <= ni < N and 0 <= nj < M:
                        if arctic[ni][nj] == 0:
                            num += 1
                if num > 0:
                    consea.append([i, j, num])
    if len(area) > 1 or len(area) == 0:
        break
    
    for sea in consea:
        arctic[sea[0]][sea[1]] -= sea[2]
        if arctic[sea[0]][sea[1]] < 0:
            arctic[sea[0]][sea[1]] = 0
    year += 1
if len(area) == 0:
    print(0)
else:
    print(year)