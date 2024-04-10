#####################접근법 봄 TIL적어야함
##################### 회의 시간이 빨리 끝나는 것부터 넣는 방식으로(만약 끝나는 시간이 같다면 먼저 시작하는 순으로 나열)
##################### 증명 : 회의 시간이 빨리 끝나야 이후 회의 시간으로 사용할 수 있는 시간이 더 많아지므로
##################### 이 방식으로 그리디하게 푸는 것이 가장 많은 회의를 할 수 있는 방법
import sys
from collections import deque

N = int(sys.stdin.readline())
meeting = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
meet = sorted(meeting, key = lambda x : (x[1], x[0]), reverse=False)
print(meet)
result = deque()

while meet:
    if not result:
        result.append(meet[0])
        meet.pop(0)
    else:
        if result[-1][1] > meet[0][0]:
            meet.pop(0)
        else:
            result.append(meet[0])
            meet.pop(0)
print(len(result))