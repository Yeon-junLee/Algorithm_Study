import sys

N = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[99999999999 for _ in range(N)] for _ in range(N)]      # dp[i][j] : i번째 matrix부터 j번째 matrix까지 곱했을 때의 최소 곱셈 연산 횟수

for i in range(N):
    dp[i][i] = 0    # 행렬이 1개면 연산 X

for i in range(N):
    for j in range(0, N - i):
        if j == j + i:      # i = 0인 경우는 행렬 j ~ j 까지의 곱만 보는 것이므로 보지 않음
            continue
        a = j
        b = j + i
        for k in range(a, b):
            dp[a][b] = min(dp[a][b], dp[a][k] + dp[k + 1][b] + matrix[a][0] * matrix[k][1] * matrix[b][1])
            # a번째 ~ b번째 행렬들을 다 곱했을 때 최소 연산 수 구하는 과정
            # a ~ k 연산 수 + k + 1 ~ b 연산 수 + 두 연산의 결과로 나온 행렬의 연산 수

print(dp[0][N - 1])