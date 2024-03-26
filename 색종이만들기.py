import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
white = 0
blue = 0

def divide(x, y, n):
    global white
    global blue
    st = paper[x][y]
    if n == 1:
        if st == 1:
            blue += 1
            return
        else:
            white += 1
            return
    flag = False
    flag2 = False
    for i in range(x, x + n):
        for j in range(y, y+ n):
            if paper[i][j] != st:
                flag = True
                break
        if flag:
            flag2 = True
            break
    if flag2:
        divide(x, y, n // 2)
        divide(x + n // 2, y, n // 2)
        divide(x, y + n // 2, n // 2)
        divide(x + n // 2, y + n // 2, n // 2)
    else:
        if st == 1:
            blue += 1
            return
        else:
            white += 1
            return

divide(0, 0, N)
print(white)
print(blue)