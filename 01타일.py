import sys

N = int(sys.stdin.readline())
if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    MAX = [0 for _ in range(N + 1)]
    MAX[1] = 1  # 1
    MAX[2] = 2  # 00 11
    #MAX[3] = 3 # 001 100 111
    #MAX[4] = 5 # 1001 0011 0000 1100 1111
    for i in range(3, N + 1):
        MAX[i] = MAX[i - 1] % 15746 + MAX[i - 2] % 15746
    print(MAX[N] % 15746)
