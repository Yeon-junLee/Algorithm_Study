#마지막문제 ##### 실패
import sys

string_T = sys.stdin.readline().strip()
string_S = sys.stdin.readline().strip()

M = len(string_T)
N = len(string_S)
MAX = 0
MAXidx = [0, 0]

lcs = [[0 for _ in range(N + 1)] for _ in range(M + 1)]

for i in range(1, M + 1):
    for j in range(1, N + 1):
        if string_T[i - 1] == string_S[j - 1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
            if MAX < lcs[i][j]:
                MAX = lcs[i][j]
                MAXidx = [i, j]
        else:
            lcs[i][j] = 0

back = MAX
answer = ""
cx = MAXidx[0]
while back > 0:
    answer = string_T[cx - 1] + answer
    back -= 1
    cx -= 1
print(MAX)
print(answer)