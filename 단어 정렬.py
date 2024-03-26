import sys

N = int(input())
li = [sys.stdin.readline() for _ in range(N)]
li.sort()
li.sort(key=len)
for i in range(N):
    if i > 0 and li[i] == li[i - 1]:
        continue
    print(li[i], end="")