import sys

M, N, L = map(int,sys.stdin.readline().split())
saro = list(map(int,sys.stdin.readline().split()))
animal = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

saro.sort()
animal.sort()

ans = 0

for i in range(len(animal)):
    if animal[i][1] > L:
        continue
    else:
        gap = L - animal[i][1]
        least = animal[i][0] - gap
        most = animal[i][0] + gap
        l = 0
        r = M - 1
        while l <= r:
            mid = (l + r) // 2
            if least <= saro[mid] <= most:
                ans += 1
                break
            elif saro[mid] < least:
                l = mid + 1
            else:
                r = mid - 1
print(ans)