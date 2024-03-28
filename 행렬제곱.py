import sys

N, B = map(int,sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def solve(M, num):
    if num == 1:
        return M
    if num == 2:
        return mpow(M, M)
    
    if num % 2:
        newM = solve(M, num//2)
        return mpow(mpow(newM, newM), M)
    else:
        newM = solve(M, num//2)
        return mpow(newM, newM)
    
def mpow(M1, M2):
    return dot(N, M1, M2)

def dot(n, m1, m2):
    ret = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ret[i][j] += m1[i][k] * m2[k][j]
            if ret[i][j] > 1000:
                ret[i][j] %= 1000
    return ret
            

ans = solve(matrix, B)
for i in range(N):
    for j in range(N):
        print(ans[i][j] % 1000, end=" ")
    print()