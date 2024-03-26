import sys

li = [int(sys.stdin.readline()) for _ in range(9)]
li.sort()
sum_li = sum(li)
over = sum_li - 100
for i in range(8):
    flag = False
    for j in range(i + 1, 9):
        total = li[i] + li[j]
        if total == over:
            a, b = li[i], li[j]
            li.remove(a)
            li.remove(b)
            flag = True
            break
    if flag:
        break
for a in li:
    print(a)