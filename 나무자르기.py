import sys

N, M = map(int,sys.stdin.readline().split())
tree = list(map(int,sys.stdin.readline().split()))

tree.sort()
l = 0
r = tree[N - 1]
ans = 0

while l <= r:
    mid = (l + r) // 2
    # print("현재 중간값 :",mid)
    total = 0
    total = sum(t - mid for t in tree if t > mid)
    # print("가져가는 나무 합 :",total)
    if total > M:
        ans = mid
        l = mid + 1
    elif total < M:
        r = mid - 1
    else:
        ans = mid
        break
print(ans)