import sys
N = int(sys.stdin.readline())
height = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False for j in range(N)] for i in range(N)]
max_height = max(map(max, height))
min_height = min(map(min, height))
MAX = 0
area = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(N):
    for j in range(N):
        print(height[i][j], end=" ")
    print()

def bfs(x, y, i):
    print("물에 잠긴 높이 :", i)
    queue = []
    visited[x][y] = True
    queue.append([x, y])
    num = 0
    while len(queue) != 0:
        cx, cy = queue.pop(0)
        num += 1
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                print(nx, ",", ny,"는 구역을 벗어남")
                continue
            if visited[nx][ny]:
                print(nx, ",", ny,"는 이미 방문함")
                continue
            if height[nx][ny] <= i:
                print(nx, ",", ny,"는 높이가 낮아서 잠김")
                continue
            # print("투입")
            print(nx, ",", ny,"는 높이가", height[nx][ny] ,"이므로 투입 가능함!")
            visited[nx][ny] = True
            queue.append([nx, ny])
    return num


for i in range(min_height, max_height):
    print("높이가",i,"일 때 구역의 개수 구하기")
    print("bfs 전 visited")
    print(visited)
    candidate = []
    for j in range(N):
        for k in range(N):
            if visited[j][k] == False and height[j][k] > i:
                print(j, "", k,"에서 bfs 시작")
                candidate.append(bfs(j, k, i))
    print("bfs 후 visited")
    print(visited)
    print(candidate)
    area.append(len(candidate))
    visited = [[False for j in range(N)] for i in range(N)]

print(max(area))