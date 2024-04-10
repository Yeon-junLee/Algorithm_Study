import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    scores = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    score1 = sorted(scores, key = lambda x : x[0])
    result = deque()
    result.append(score1[0])
    for i in range(1, N):
        if score1[i][1] < result[-1][1]:
            result.append(score1[i])
    print(len(result))