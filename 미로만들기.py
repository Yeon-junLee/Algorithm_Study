##########################################################접근법 참고 => TIL 에 작성해야함###########################################################
############################################################최초 방법은 메모리 초과 났었음###########################################################
#################heapq를 쓰는 방법 외에 visited 배열을 이용해 현재까지 뚫고 온 벽의 개수를 비교하여 더 작은 것을 저장해 나가는 방식도 존재#################
import sys
import heapq

def bfs(x, y):
    global MIN
    hq = []
    heapq.heappush(hq, [0, x, y])
    visited[x][y] = True
    while len(hq):
        cost, cx, cy = heapq.heappop(hq)
        if cx == N - 1 and cy == N - 1:
            MIN = cost
            break

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == False:
                    if maze[nx][ny] == '1':
                        heapq.heappush(hq, [cost, nx, ny])
                    else:
                        heapq.heappush(hq, [cost + 1, nx, ny])
                    visited[nx][ny] = True

N = int(sys.stdin.readline())
maze = [list(str(sys.stdin.readline().strip())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
MIN = 999999999999
bfs(0, 0)
print(MIN)