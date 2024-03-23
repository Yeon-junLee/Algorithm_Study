answer = 0
cantcol = []
def dfs(chess, row):
    global answer
    print("@@@@@@@@@@@@@@@@@@@@@@@@@현재 ROW :", row, "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("현재 체스판 상태")
    n = len(chess)
    for i in range(n):
        for j in range(n):
            print(chess[i][j], end=" ")
        print()

    ### column 하나씩 바꿔보며 확인
    for i in range(n):
        ### 겹치는 column 있는지 확인
        if i in cantcol:
            continue

        chess[row][i] = 1
        flag = False
        ### 오른쪽 위 대각선 확인
        for j in range(1, n - 1):
            next_row = row - j
            next_col = i + j
            if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n:
                break
            if chess[next_row][next_col] == 1:
                flag = True
                break
        ### 오른쪽 아래 대각선 확인
        for j in range(1, n - 1):
            if flag is True:
                break
            next_row = row + j
            next_col = i + j
            if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n:
                break
            if chess[next_row][next_col] == 1:
                flag = True
                break
        ### 왼쪽 위 대각선 확인
        for j in range(1, n - 1):
            if flag is True:
                break
            next_row = row - j
            next_col = i - j
            if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n:
                break
            if chess[next_row][next_col] == 1:
                flag = True
                break
        ### 왼쪽 아래 대각선 확인
        for j in range(1, n - 1):
            if flag is True:
                break
            next_row = row + j
            next_col = i - j
            if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n:
                break
            if chess[next_row][next_col] == 1:
                flag = True
                break
        if flag is True:
            chess[row][i] = 0
            continue
        else:
            ### 마지막 row인지 확인
            if row == n - 1:
                print("정답 추가")
                for i in range(n):
                    for j in range(n):
                        print(chess[i][j], end=" ")
                    print()
                answer += 1
                chess[row][i] = 0
                return
            else:
                cantcol.append(i)
                dfs(chess, row + 1)
                chess[row][i] = 0
                cantcol.remove(i)

N = int(input())
chess = [[0 for j in range(N)] for i in range(N)]

if N <= 3:
    print(0)
else:
    dfs(chess, 0)
    print(answer)