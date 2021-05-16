n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(input())
result = []

# 행고정
for i in range(n-7):
    # 열고정
    for j in range(m-7):
        first_W = 0
        first_B = 0
        for k in range(i,i+8):
            for l in range(j,j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        first_W += 1
                    if board[k][l] != 'B':
                        first_B += 1
                else:
                    if board[k][l] != 'B':
                        first_W += 1
                    if board[k][l] != 'W':
                        first_B += 1
        result.append(first_W)
        result.append(first_B)

print(min(result))