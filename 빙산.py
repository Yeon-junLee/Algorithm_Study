import sys

def bfs(x, y):
    a = 0
    queue = []
    queue.append([x, y])
    visited[x][y] = True
    while queue:
        cx = queue[0][0]
        cy = queue[0][1]
        queue.pop(0)
        a += 1
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == False:
                    queue.append([nx, ny])
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

    for i in range(N):
        for j in range(M):
            if visited[i][j] == False and arctic[i][j] > 0:
                area.append(bfs(i, j))
            if arctic[i][j] > 0:
                num = 0
                for i in range(4):
                    ni = i + dx[i]
                    nj = j + dy[i]
                    if 0 <= ni < N and 0 <= nj < M:
                        if arctic[ni][nj] == 0:
                            num += 1
                consea.append([i, j, num])
    if len(area) > 1:
        break
    
    for sea in consea:
        arctic[sea[0]][sea[1]] -= sea[2]
        if arctic[sea[0]][sea[1]] < 0:
            arctic[sea[0]][sea[1]] = 0

    year += 1

print(year)