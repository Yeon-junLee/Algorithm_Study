import sys
N = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
check = list(map(int,sys.stdin.readline().split()))
li.sort()

def bsearch(target):
    l = 0
    r = N - 1
    while l <= r:
        mid = (l + r) // 2
        if li[mid] < target:
            l = mid + 1
        elif li[mid] > target:
            r = mid - 1
        else:
            return True
    return False
    

for i in range(M):
    if bsearch(check[i]):
        print(1)
    else:
        print(0)