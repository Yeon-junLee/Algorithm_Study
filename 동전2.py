import sys

n, k = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(n)]

dp = [999999999 for _ in range(k + 1)]

dp[0] = 0
coin.sort()
for c in coin:
    if c > k:
        break
    dp[c] = 1

for i in range(1, k + 1):
    for c in coin:
        if i >= c:
            dp[i] = min(dp[i], dp[i - c] + dp[c])
if dp[k] == 999999999:
    print(-1)
else:
    print(dp[k])