import sys

N = int(input())
li = [int(sys.stdin.readline()) for _ in range(N)]
li.sort()
for a in li:
    print(a)