import sys
N = int(sys.stdin.readline())
tower = list(map(int,sys.stdin.readline().split()))

stack = []
ans = [0 for _ in range(N)]
for i in range(N - 1, -1, -1):
    if len(stack) > 0:
        while stack[-1][1] <= tower[i]:
            loc = stack[-1][0]
            ans[loc] = i + 1
            stack.pop()
            if len(stack) == 0:
                break
    stack.append([i, tower[i]])
while len(stack) > 0:
    loc = stack[-1][0]
    ans[loc] = 0
    stack.pop()

for i in ans:
    print(i, end=" ")