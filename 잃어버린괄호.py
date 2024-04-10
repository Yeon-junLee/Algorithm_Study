import sys

formula = str(sys.stdin.readline().strip())
operator = []
for a in formula:
    if a == '+':
        operator.append(a)
    elif a =='-':
        operator.append(a)
val = formula.replace('+', '-').split('-')
for i in range(len(val)):
    val[i] = int(val[i])
    total = 0
minus_idx = []

if '-' not in operator:
    for num in val:
        total += num
else:
    for i in range(len(operator)):
        if operator[i] == '+':
            # print(i, "번째 연산자가 +이므로", i + 1, "번째 수와", i, "번째 수를 더함")
            val[i + 1] += val[i]
        else:
            # print(i, "번째 연산자가 -이므로", i + 1, "번째 수로 넘어감")
            minus_idx.append(i)
        if i == len(operator) - 1:
            minus_idx.append(i + 1)
    total += val[minus_idx[0]]
    for i in range(1, len(minus_idx)):
        total -= val[minus_idx[i]]

print(total)