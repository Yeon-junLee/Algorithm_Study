import sys

N, K = map(int, sys.stdin.readline().split())

A = [int(sys.stdin.readline()) for _ in range(N)]

ans = 0
idx = N - 1
while K > 0:
    if K >= A[idx]:
        ans += (K // A[idx])
        K -= A[idx] * (K // A[idx])
    else:
        idx -= 1
print(ans)