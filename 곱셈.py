import sys

a, b, c = map(int,sys.stdin.readline().split())

a %= c

def modulo(A, B, C):
    if B == 0:
        return 1
    if B == 1:
        return A % C
    
    if B % 2 == 0:
        return (modulo(A, B // 2, C) ** 2) %  C
    else:
        return (modulo(A, B // 2, C) ** 2) * modulo(A, 1, C) % C
    
print(modulo(a, b, c))