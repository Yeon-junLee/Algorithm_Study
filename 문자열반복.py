T = int(input())
for i in range(T):
    a, b = input().split()
    a = int(a)
    string = ''
    for char in b:
        for j in range(a):
            string = string + char
    print(string)