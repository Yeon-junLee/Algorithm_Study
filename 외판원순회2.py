import sys

def dfs(start, now, cost, cnt):
    global ans
    if cnt == N:
        if town[now][start]:
            cost += town[now][start]
            if ans > cost:
                ans = cost
        return
    
    if cost > ans:
        return
    
    for i in range(N):
        if visited[i] == False and town[now][i]:
            visited[i] = True
            dfs(start, i, cost + town[now][i], cnt + 1)
            visited[i] = False


N = int(sys.stdin.readline())
town = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [False] * N
ans = sys.maxsize

for i in range(N):
    visited[i] = True
    dfs(i, i, 0, 1)
    visited[i] = False
print(ans)



############################# 다른 코드 #################################
# import sys
# N = int(sys.stdin.readline())

# town = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# visited = [False] * N
# ans = 999999999

# def dfs(start, cost):
#     global ans
#     if False not in visited:
#         if town[start][0] == 0:
#             return
#         tozero = cost + town[start][0]
#         if ans > tozero:
#             ans = tozero
#             return
#         return
    
#     if cost > ans:
#         return
    
#     for i in range(N):
#         # print(i,"번째 마을 확인")
#         if visited[i]:
#             continue
#         if town[start][i] == 0:
#             continue
        
#         visited[i] = True
#         dfs(i, cost + town[start][i])
#         visited[i] = False

# visited[0] = True
# dfs(0, 0)
# print(ans)