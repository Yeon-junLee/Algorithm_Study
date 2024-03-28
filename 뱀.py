import sys
from collections import deque

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
apple = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
L = int(sys.stdin.readline())
change = [list(sys.stdin.readline().split()) for _ in range(L)]

snake = deque()
snake.append([0, 0])
dir = [0, 1]
time = 0
idx = 0
### change의 인덱스 체크(change pop하면 추가 연산)
while snake[0][0] >= 0 and snake[0][0] < N and snake[0][1] >= 0 and snake[0][1] < N:
    if len(change) > idx:
        if time == int(change[idx][0]):
            if dir == [0, 1]:
                if change[idx][1] == 'L':
                    dir = [-1, 0]
                else:
                    dir = [1, 0]
            elif dir == [-1, 0]:
                if change[idx][1] == 'L':
                    dir = [0, -1]
                else:
                    dir = [0, 1]
            elif dir == [0, -1]:
                if change[idx][1] == 'L':
                    dir = [1, 0]
                else:
                    dir = [-1, 0]
            else:
                if change[idx][1] == 'L':
                    dir = [0, 1]
                else:
                    dir = [0, -1]
            idx += 1
    nx = snake[0][0] + dir[0]
    ny = snake[0][1] + dir[1]
    if [nx, ny] in snake:
        time += 1
        break
    snake.appendleft([nx, ny])
    if [nx + 1, ny + 1] in apple:
        apple.remove([nx + 1, ny + 1])
    else:
        snake.pop()
    time += 1
print(time)