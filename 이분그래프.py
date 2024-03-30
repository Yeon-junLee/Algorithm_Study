import sys

def bfs(node):
    queue = []
    color[node] = 0
    queue.append(node)
    while queue:
        cur = queue[0]
        queue.pop(0)
        # print("현재 노드",cur,"의 색 :", color[cur])
        for next in edge[cur]:
            if color[next] != -1:
                # print("next인",next ,"의 색 :",color[next])
                if color[next] == color[cur]:
                    # print("다음 거랑 색이 같아서 불가능")
                    return False
                else:
                    continue
            else:
                color[next] = (color[cur] + 1) % 2
                queue.append(next)
    return True

K = int(sys.stdin.readline())

for i in range(K):
    V, E = map(int, sys.stdin.readline().split())

    edge = [[] for _ in range(V + 1)]
    for i in range(E):
        a, b= map(int, sys.stdin.readline().split())
        edge[a].append(b)
        edge[b].append(a)
    color = [-1 for _ in range(V + 1)]
    flag = True
    for i in range(1, V + 1):
        if color[i] == -1:
            flag = bfs(i)
            if flag == False:
                break
    if flag:
        print("YES")
    else:
        print("NO")
    