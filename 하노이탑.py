import sys
sys.setrecursionlimit(10**5)

def hanoi(answer, N, start, mid, end):
    if N == 0:
        return
    hanoi(answer, N - 1, start, end, mid)
    answer.append([start, end])
    hanoi(answer, N - 1, mid, start, end)

N = int(input())
total = 2 ** N - 1
### N-1개를 옮길 때와 N개를 옮길 때의 차이를 구분해야함
### N개를 옮기는 것은 N - 1개를 2로 옮기고 마지막 판을 옮긴 뒤, 다시 N - 1개를 옮기는 것이므로
### num(N) = num(N - 1) * 2 + 1
### 점화식화 하면 An = 2^n - 1
answer = []
if N <= 20:
    hanoi(answer, N, 1, 2, 3)
print(total)
if N <= 20:
    for move in answer:
        print(move[0], move[1])