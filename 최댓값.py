import sys

li = []
for i in range(9):
    num = int(input())
    li.append(num)

print(max(li))
print(li.index(max(li)) + 1)