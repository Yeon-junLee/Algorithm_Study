import sys
import heapq

N = int(sys.stdin.readline())
li = []
for i in range(N):
    a, b = map(int,sys.stdin.readline().split())
    li.append([min(a, b), max(a, b)])
d = int(sys.stdin.readline())
li.sort(key = lambda x : (x[1], x[0]))
### 사람들 집~회사를 더 뒤에 있는거 기준으로 오름차순, 같다면 앞에 있는거 기준으로 오름차순

hq = []
ans = 0
for i in range(N):
    start_point = li[i][1] - d
    ### end_point를 기준으로 d 만큼 뺀 것을 기준으로 삼음
    heapq.heappush(hq, li[i][0])
    ### min heap에 지금 사람의 집(start 지점)을 넣음
    while hq and hq[0] < start_point:
        ### min heap이 비어있지 않고, min heap의 첫번째 값이 기준점보다 앞에 있다면 min heap에서 제거
        heapq.heappop(hq)
    ### min heap 안에 있는 점들은 현재 기준점보다 뒤에 있으므로 더 처리 해줄게 없음
    ans = max(ans, len(hq))
    ### heap의 크기와 현재 정답을 비교
print(ans)