N = int(input())
prime = [True for i in range(10001)]
prime[0] = False
prime[1] = False
for i in range(2, 10001):
    for j in range(i * i, 10001, i):
        prime[j] = False
for i in range(N):
    num = int(input())
    MIN = 999999
    answer = []
    for i in range(2, num // 2 + 1):
        if prime[i] is False:
            continue
        if prime[num - i] is False:
            continue
        if(abs(num - i - i) < MIN):
            MIN = abs(num - i - i)
            answer = [i, num- i]
    print(answer[0], answer[1])