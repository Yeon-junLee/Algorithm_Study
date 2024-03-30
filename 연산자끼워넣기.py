import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
operator = list(map(int, sys.stdin.readline().split()))     #[인덱스별 연산자] 0 : +, 1 : -, 2 : *, 3 : /
visited = [False for _ in range(N)]
MAX = -9999999999
MIN = 9999999999
def dfs(num_idx, num):
    global MAX
    global MIN
    if num_idx == N:
        MAX = max(MAX, num)
        MIN = min(MIN, num)
        return
    for i in range(4):
        if operator[i] > 0:
            if i == 0:
                operator[i] -= 1
                dfs(num_idx + 1, num + A[num_idx])
                operator[i] += 1
            elif i == 1:
                operator[i] -= 1
                dfs(num_idx + 1, num - A[num_idx])
                operator[i] += 1
            elif i == 2:
                operator[i] -= 1
                dfs(num_idx + 1, num * A[num_idx])
                operator[i] += 1
            else:
                operator[i] -= 1
                if num < 0:
                    result = -num // A[num_idx]
                    dfs(num_idx + 1, -result)
                else:
                    dfs(num_idx + 1, num // A[num_idx])
                operator[i] += 1
dfs(1, A[0])
print(MAX)
print(MIN)