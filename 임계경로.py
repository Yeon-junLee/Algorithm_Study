###################################################접근법 및 정답 확인 TIL 작성 필수#######################################################
########################접근법 : 각 노드 별로 거기까지 오는데 걸리는 최대 시간을 저장하는 배열을 선언해서 maxTime 찾음###########################
########################도착 노드에서 역 순회를 하면서 maxT - 도로에서 걸린 시간 == 이전 노드 최대 시간 이면 답 + 1##############################
##끝에서 처음으로 돌아갈 때 outdegree를 이용하여 위 조건에 해당되고 outdegree가 0인 경우에만 queue에 삽입하는 방식으로 이미 갔던 도로 안겹치게 순회하도록 했는데 틀림#######
###################정답 : visited 리스트를 이용하여 이미 방문한 노드면 다시 그 도로로 안돌아가게 해서 중복 해결##################################
import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

indegree = [0 for _ in range(n + 1)]
edge = [[] for _ in range(n + 1)]
revedge = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edge[a].append([b, c])
    revedge[b].append([a, c])
    indegree[b] += 1
start, end = map(int, sys.stdin.readline().split())

anstime = 0
ansroute = 0
queue = deque(maxlen = 10000)     ### 현재 노드 정보
maxT = [0 for _ in range(n + 1)]    ### index번 노드까지 오는데 걸린 최대 시간

queue.append(start)
while queue:
    cur = queue.popleft()
    for next in edge[cur]:
        nnode = next[0]
        ntime = next[1]
        indegree[nnode] -= 1
        maxT[nnode] = max(maxT[cur] + ntime, maxT[nnode])
        if indegree[nnode] == 0:
            queue.append(nnode)

anstime = maxT[end]
queue.clear()
queue.append(end)
visited = [False for _ in range(n + 1)]

while queue:
    cur = queue.popleft()
    for prev in revedge[cur]:
        pnode = prev[0]
        ptime = prev[1]
        if maxT[cur] - ptime == maxT[pnode]:
            ansroute += 1
            if visited[pnode]:
                continue
            queue.append(pnode)
            visited[pnode] = True

print(anstime)
print(ansroute)