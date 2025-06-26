### 백준 2636: 치즈

from collections import deque 
row, column = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(row)]

#상하좌우
dx = [-1, 1, 0, 0] #상하
dy = [0, 0, -1, 1] #좌우

def bfs():
    queue = deque()
    queue.append((0, 0))
    visited = [[False]*column for _ in range(row)]
    visited[0][0] = True
    melt = []
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<row and 0<=ny<column and not visited[nx][ny]:
                visited[nx][ny] = True
                if grid[nx][ny] == 0:
                    queue.append((nx, ny))
                elif grid[nx][ny] == 1:
                    melt.append((nx, ny))
                    
    for x, y in melt:
        grid[x][y] = 0
    return len(melt)
                

time = 0
last_cnt = 0

while True:
    melted_cheese = bfs()
    if melted_cheese == 0: 
        break
    last_cnt = melted_cheese
    time += 1

print(time)
print(last_cnt)