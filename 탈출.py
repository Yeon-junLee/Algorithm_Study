import sys
from collections import deque

def bfs():
    global MIN
    w = deque()
    h = deque()

    for pos in water:
        wx, wy = pos
        w.append((wx, wy, 0))
    h.append((startx, starty, 0))
    visited[startx][starty] = True
    time = 0
    flag = False
    while True:
        while h:
            if h[0][2] != time:
                break
            cx, cy, ct = h.popleft()
            if forest[cx][cy] == '*':
                continue
            
            if forest[cx][cy] == 'D':
                MIN = min(MIN, ct)
                flag = True
                break

            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                
                if 0 <= nx < R and 0 <= ny < C:
                    if visited[nx][ny]:
                        continue
                    if forest[nx][ny] == '*' or forest[nx][ny] == 'X':
                        continue
                    h.append((nx, ny, ct + 1))
                    visited[nx][ny] = True
        if not h:
            return
        if flag:
            break
        while w:
            if w[0][2] != time:
                break
            wcx, wcy, wct = w.popleft()
            
            for i in range(4):
                wnx = wcx + dx[i]
                wny = wcy + dy[i]

                if 0 <= wnx < R and 0 <= wny < C:
                    if forest[wnx][wny] == '*' or forest[wnx][wny] == 'D' or forest[wnx][wny] == 'X':
                        continue
                    forest[wnx][wny] = '*'
                    w.append((wnx, wny, wct + 1))
        time += 1
               

R, C = map(int, sys.stdin.readline().split())
forest = [list(str(sys.stdin.readline().strip())) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]
water = []
startx = 0
tarty = 0
for i in range(R):
    for j in range(C):
        if forest[i][j] == '*':
            water.append((i, j))
        if forest[i][j] == 'S':
            startx = i
            starty = j
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
MIN = 9999999999999
bfs()
if MIN == 9999999999999:
    print("KAKTUS")
else:
    print(MIN)