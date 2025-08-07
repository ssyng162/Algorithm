### 백준 1285: 동전 뒤집기

def flip_rows(board, mask):
    N = len(board)
    tmp = [row[:] for row in board]
    for i in range(N):
        if (mask >> i) & 1:
            for j in range(N):
                tmp[i][j] = 1 - tmp[i][j]
    return tmp

def count_min_t(board):
    N = len(board)
    total = 0
    for i in range(N):
        h = 0
        t = 0
        for j in range(N):
            if board[j][i] == 0:
                h += 1
            else:
                t += 1
        total += min(h, t)
    return total

N = int(input())
coins = [list(input().strip()) for _ in range(N)]
board = [[0 if c == 'H' else 1 for c in row] for row in coins]

result = float('inf')
for mask in range(1 << N):
    flipped_board = flip_rows(board, mask)
    result = min(result, count_min_t(flipped_board))

print(result)