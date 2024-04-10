import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())

    dp = [0 for _ in range(M + 1)]
    dp[0] = 1
    for coin in coins:                      # 처음 할 때, coin for문과 돈 액수 for문 순서가 반대여서 중복처리가 안됨
        for i in range(M + 1):              # coin에 대해서 먼저 돌면 중복 처리가 됨(순서가 정해진 상태로 돌기 때문에)
            if i - coin >= 0:
                dp[i] += dp[i - coin]
    print(dp[M])