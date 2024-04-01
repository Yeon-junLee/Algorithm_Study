import sys
from collections import deque

def bfs():
    global MIN
    q = deque()
    days = deque()
    for ripe in ripen:
        x, y, z = ripe
        visited[z][y][x] = True
        q.append((x, y, z))
        days.append(0)

    while q:
        cx, cy, cz = q.popleft()
        cd = days.popleft()

        MIN = max(MIN, cd)

        for i in range(6):
            nx = cx + dx[i]
            ny = cy + dy[i]
            nz = cz + dz[i]

            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
                if visited[nz][ny][nx] == False:
                    if tomato[nz][ny][nx] == 1:
                        visited[nz][ny][nx] = True
                        continue
                    elif tomato[nz][ny][nx] == -1:
                        visited[nz][ny][nx] = True
                        continue
                    else:
                        tomato[nz][ny][nx] = 1
                        visited[nz][ny][nx] = True
                        q.append((nx, ny, nz))
                        days.append(cd + 1)
                        

M, N, H = map(int, sys.stdin.readline().split())
tomato = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]
MIN = -1
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
dz = [-1 ,1, 0, 0, 0, 0]
ripen = []
flag = False
## 접근할때 tomato[h][row][col]

for i in range(M):
    for j in range(N):
        for k in range(H):
            if tomato[k][j][i] == 1:
                ripen.append((i, j, k))
            if tomato[k][j][i] == 0:
                flag = True
if flag:
    flag1 = False
    flag2 = False
    flag3 = False
    bfs()
    for i in range(M):
        for j in range(N):
            for k in range(H):
                if tomato[k][j][i] == 0:
                    flag3 = True
                    break
            if flag3:
                flag2 = True
                break
        if flag2:
            flag1 = True
            break
    if flag1:
        print(-1)
                    
    else:
        print(MIN)
else:
    print(0)