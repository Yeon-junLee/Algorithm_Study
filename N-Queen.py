N = int(input())

def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(x - i) == abs(row[x] - row[i]):
            ### 같은 column에 있는지 확인 || 대각선에 같이 있는지 확인
            return False
    return True

def dfs(x):
    global answer
    if x == N:
        answer += 1
    else:
        for i in range(N):
            row[x] = i
            if check(x):
                dfs(x + 1)
answer = 0
row = [0] * N
dfs(0)
print(answer)