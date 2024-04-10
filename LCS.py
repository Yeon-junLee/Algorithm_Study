import sys

string_A = sys.stdin.readline().strip()
string_B = sys.stdin.readline().strip()
M = len(string_A)
N = len(string_B)

LCS = [[0 for _ in range(N + 1)] for _ in range(M + 1)]

for i in range(1, M + 1):
    for j in range(1, N + 1):
        if string_A[i - 1] == string_B[j - 1]:      # stringA의 i번째 문자와 stringB의 j번째 문자가 같다면
            LCS[i][j] = LCS[i - 1][j - 1] + 1       # LCS배열의 i-1, j-1 번째 값에 + 1 시킴
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])       # 다르면 그냥 위 아래 값중에 최대값 고름
print(LCS[M][N])