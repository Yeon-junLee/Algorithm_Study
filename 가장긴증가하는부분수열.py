import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

DP = [0 for _ in range(N)]
DP[0] = 1
for i in range(1, N):
    # print("현재 수 :",A[i])
    # print(DP)
    MAX = 0
    for j in range(i - 1, -1, -1):
        # print(j, "번째 수 :",A[j])
        if A[j] < A[i]:
            # print("MAX 값 :", MAX, ",", j,"의 DP값 :",DP[j])
            MAX = max(MAX, DP[j])
    DP[i] = MAX + 1
print(max(DP))