#################################################접근법 확인했기 때문에 TIL 알고리즘에 적어야함#######################################################################
################################ 이전 아이디어는 모든 실내 공간에 대해 다음 실내 공간까지의 루트를 탐색했고 시간초과가 났었음#############################################

import sys
sys.setrecursionlimit(10**7)
# dfs 방식 (접근 참고)
# def dfs(start):
#     inside = 0
#     for next in edge[start]:
#         if A[next - 1] == '0':
#             if visited[next] == False:
#                 visited[next] = True
#                 inside += dfs(next)
#         else:
#             inside += 1
#     return inside

# bfs 방식 (원래 내 방식)
def bfs(start):
    inside = 0
    queue = []
    queue.append(start)
    while queue:
        cur = queue[0]
        queue.pop(0)
        for next in edge[cur]:
            if A[next - 1] == '0':
                if visited[next] == False:
                    visited[next] = True
                    queue.append(next)
            else:
                inside += 1
    return inside

N = int(sys.stdin.readline())
A = list(str(sys.stdin.readline().strip()))     # A[i] = 1 이면 실내, 0 이면 실외
edge = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
ans = 0

for i in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    edge[a].append(b)
    edge[b].append(a)
    if A[a - 1] == '1' and A[b - 1] == '1':     # 실내 to 실내가 가능하므로 두가지 경우의 수 추가
        ans += 2

for i in range(1, N + 1):
    inside = 0
    if A[i - 1] == '0':     # 실내 공간에서 탐색을 시작하는 것이 아닌, 실외 공간에서 연결된 실내 공간 개수를 조사
        if visited[i] == False:
            visited[i] = True
            # inside = dfs(i)       # dfs 방식(답 참고)
            inside = bfs(i)         # bfs 방식(내 방식)
    ans += inside * (inside - 1)        # 하나의 실내 공간에 연결되어있는 실내 공간에 대해, 순서 관계없이 실내 공간 2가지를 고르는 경우의 수 추가

print(ans)