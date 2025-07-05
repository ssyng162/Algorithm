### 백준 1987: 알파벳

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def count(x, y):
    queue = set()
    queue.add((x, y, board[x][y]))
    cnt = 0

    while queue:
        x, y, visited = queue.pop()

        cnt = max(cnt, len(visited))
        if cnt == 26:
            return 26

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<row and 0<=ny<column and board[nx][ny] not in visited:
                queue.add((nx, ny, visited + board[nx][ny]))

    return cnt

row, column = map(int, input().split())
board = [list(input().strip()) for _ in range(row)]
print(count(0, 0))