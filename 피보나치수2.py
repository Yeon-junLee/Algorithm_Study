import sys
n = int(sys.stdin.readline())
fibo = [0 for _ in range(n + 1)]
if n == 0:
    print(0)
elif n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    fibo[1] = 1
    fibo[2] = 1
    for i in range(3, n + 1):
        fibo[i] = fibo[i - 1] + fibo[i - 2]
    print(fibo[n])