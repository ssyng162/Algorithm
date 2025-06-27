### 백준 2589: 보물섬

from collections import deque

row, column = map(int, input().split())
treasure_map = [list(input().strip()) for _ in range(row)]

#상하좌우
dx = [-1, 1, 0, 0] #상하
dy = [0, 0, -1, 1] #좌우

def bfs(start_x, start_y):
    dist = [[-1]*column for _ in range(row)]
    queue = deque()
    queue.append((start_x, start_y))
    dist[start_x][start_y] = 0
    max_dist = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not 0<=nx<row or not 0<=ny<column:
                continue
            if treasure_map[nx][ny] == 'L' and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                max_dist = max(max_dist, dist[nx][ny])
                queue.append((nx, ny))
    return max_dist

result = 0
for i in range(row):
    for j in range(column):
        if treasure_map[i][j] == 'L':
            result = max(result, bfs(i, j))
    
print(result)