### 백준 4179: 불!

from collections import deque
row, column = map(int, input().split())
maze = [list(input().strip()) for _ in range(row)]

#상하좌우
dx = [-1, 1, 0, 0] #상하
dy = [0, 0, -1, 1] #좌우

def is_escaped(x, y):
    return x==0 or x==row-1 or y==0 or y==column-1

def is_valid_move(x, y):
    return 0<=x<row and 0<=y<column

f_queue = deque()
j_queue = deque()

fire = [[-1]*column for _ in range(row)]
dist = [[-1]*column for _ in range(row)]

start_x = start_y = -1
for i in range(row):
    for j in range(column):
        if maze[i][j] == 'J':
            j_queue.append((i, j))
            dist[i][j] = 0
            start_x, start_y = i, j
        if maze[i][j] == 'F':
            f_queue.append((i, j))
            fire[i][j] = 0

if is_escaped(start_x, start_y):
    print(1)
    exit()

            
def fire_bfs():
    while f_queue:
        x, y = f_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not is_valid_move(nx, ny): 
                continue
            if maze[nx][ny] == '#' or fire[nx][ny] != -1:
                continue
            fire[nx][ny] = fire[x][y] + 1
            f_queue.append((nx, ny))
            
                

def j_bfs():
    while j_queue:
        x, y = j_queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if is_escaped(x, y):
                return dist[x][y]+1
            if not is_valid_move(nx, ny):
                continue
            if maze[nx][ny] == '#':
                continue
            if dist[nx][ny] != -1:
                continue
            if fire[nx][ny] != -1 and fire[nx][ny] <= dist[x][y] + 1:
                continue
            dist[nx][ny] = dist[x][y] + 1
            j_queue.append((nx, ny))
    return 'IMPOSSIBLE'    

fire_bfs()
print(j_bfs())