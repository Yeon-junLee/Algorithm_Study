import sys
from collections import deque

N, K = map(int,sys.stdin.readline().split())

### queue(deque) 사용한 코드
josepus = []
circle = deque()
for i in range(1, N + 1):
    circle.append(i)

while circle:
    for i in range(K - 1):
        circle.append(circle.popleft())
    josepus.append(circle.popleft())
print("<",end="")
for i in range(len(josepus)):
    if i != len(josepus) - 1:
        print(josepus[i], end=", ")
    else:
        print(josepus[i], end="")
print(">")

### queue 사용하지 않은 코드
# circle = [i for i in range(1, N + 1)]
# turn = -1
# josepus = []
# while len(circle) > 0:
#     turn += K
#     while turn >= len(circle):
#         turn -= len(circle)
#     josepus.append(circle[turn])
#     circle.pop(turn)
#     turn -= 1

# print("<",end="")
# for i in range(len(josepus)):
#     if i != len(josepus) - 1:
#         print(josepus[i], end=", ")
#     else:
#         print(josepus[i], end="")
# print(">")