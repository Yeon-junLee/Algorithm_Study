import sys

N, K = map(int, sys.stdin.readline().split())
obj = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

knapsack = [[0 for _ in range(K + 1)] for _ in range(N)]    # 행 : 물건의 index, 열 : 가방에 담을 수 있는 최대 무게
for i in range(K + 1):
    if i >= obj[0][0]:
        knapsack[0][i] = obj[0][1]

for i in range(1, N):
    for j in range(K + 1):
        if j - obj[i][0] >= 0:      # 만약 가방에 담을 수 있는 최대 무게가 jkg이고, i번째 물건의 무게가 j이하인 경우
            knapsack[i][j] = max(knapsack[i - 1][j], obj[i][1] + knapsack[i - 1][j - obj[i][0]])    # 이전 물건까지 봤을 때 최대 가치 vs 이전 물건 안담고 이번 물건 담았을 때 가치
        else:
            knapsack[i][j] = knapsack[i - 1][j]
print(knapsack[N - 1][K])