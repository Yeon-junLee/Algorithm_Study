import sys

N, M = map(int, sys.stdin.readline().split())
maxnum = int((2 * N) ** 0.5)    # 최대로 움직일 수 있는 칸 수
rockb = [[int(1e9) for _ in range(maxnum + 2)] for _ in range(N + 1)]       # rockb[i][j] : i번째 돌로 v의 속도로 왔을 때의 최소값
cant = [int(sys.stdin.readline()) for _ in range(M)]

rockb[1][0] = 0

for i in range(2, N + 1):
    if i in cant:
        continue
    for j in range(1, int((2 * i) ** 0.5) + 1):
        rockb[i][j] = min(rockb[i - j][j - 1], rockb[i - j][j], rockb[i - j][j + 1]) + 1 
        # i - j번째 돌에 j - 1, j, j + 1의 속도로 왔으면 각각 j의 속도로 i로 올 수 있음 

if min(rockb[N]) >= int(1e9):
    print(-1)
else:
    print(min(rockb[N]))