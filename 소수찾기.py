N = int(input())
li = list(input().split())
prime = [True for i in range(1001)]
prime[0] = False
prime[1] = False
for i in range(2, 1001):
    for j in range(i * i, 1001, i):
        prime[j] = False
answer = 0
for num in li:
    if prime[int(num)]:
        answer += 1
print(answer)