##########################################################접근법 참고 => TIL 에 작성해야함###########################################################
####################################################최초 방법(탑 다운 방식)은 메모리 초과 났었음######################################################
#################################################탑 다운을 위상정렬 후 DP 배열을 통해 풀었으면 됐을 듯##################################################
import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

indegree = [0 for _ in range(N + 1)]
edge = [[] for _ in range(N + 1)]

for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    edge[b].append((a, c))  # a를 만드는데 b가 c개 필요하다.
    indegree[a] += c

need = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
base = []
queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)
        base.append(i)
for node in base:
    need[node][node] = 1
    
while queue:
    cur = queue.popleft()
    for [next, num] in edge[cur]:     ### cur과 연결된 next를 만들기 위해서는 cur이 num개 필요
        for j in range(1, N + 1):
            need[next][j] += need[cur][j] * num
        indegree[next] -= num

        if indegree[next] == 0:
            queue.append(next)
for node in base:
    print(node, need[N][node])