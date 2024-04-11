import sys

INF = 999999999

def dfs(cur, visited):
    if visited == (1 << N) - 1:     # 1이 N개가 있다는 것은 N개의 노드를 모두 방문했다는 의미
        if edge[cur][0] == 0:       # 만약 시작 노드인 0으로 돌아가는 길이 없다면
            return INF              # INF를 return해서 이 경로는 잘못 됐다는 것을 알려줌
        return edge[cur][0]         # 전부 다 방문된 경우에는 0번 노드로 돌아가는 길의 cost를 반환하여 호출 함수에서 계산이 되도록
    
    if dp[cur][visited] != -1:      # 현재 상황이 이미 방문되어서 최적화가 된 상황이라면(이 dp 값이 존재한다는 것은 바닥까지 내려와서 최적화가 완료되었다는 의미)
        return dp[cur][visited]     # 최적화된 것을 return해줌
    
    dp[cur][visited] = INF          # 현 상황 방문 표시

    for i in range(N):
        if visited & (1 << i) == 1 << i:        # i 번째 노드가 방문했는지 확인(&연산자로 인해 visited에서 i번째 숫자가 1이라면 i번째 노드는 이미 방문했다는 의미)
            continue
        if edge[cur][i] == 0:                   # cur노드에서 i번 노드로 가는 경로가 없는 경우는 continue
            continue 
        dp[cur][visited] = min(dp[cur][visited], edge[cur][i] + dfs(i, visited | 1 << i))       # i번 노드를 통해가는 경우가 존재하는지(존재하지 않으면 INF return), 존재한다면 최적의 해인지(min을 통해) 한번에 확인 
    return dp[cur][visited]         # dp 시작하는 요소에 정보가 전부 담겨져서 돌아옴

N = int(sys.stdin.readline())
edge = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[-1 for _ in range(1 << 16)] for _ in range(16)]

print(dfs(0, 1))