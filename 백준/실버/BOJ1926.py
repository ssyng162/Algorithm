### 백준 1926: 그림

from collections import deque

#상하좌우
dx = [-1, 1, 0, 0] #상하
dy = [0, 0, -1, 1] #좌우

def bfs(x, y):
    queue = deque()
    visited[x][y] = True
    queue.append((x, y))
    area = 1
    
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if not 0<=nx<row or not 0<=ny<column:
                continue
            if paper[nx][ny] == 0:
                continue
            if visited[nx][ny]:
                continue
            
            
            visited[nx][ny] = True
            queue.append((nx, ny))
            area += 1
    return area

row, column = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(row)]
visited = [[False]*column for _ in range(row)]
cnt = 0
max_area = 0

for r in range(row):
    for c in range(column):
        if paper[r][c] == 1 and not visited[r][c]:
            cnt += 1
            max_area = max(max_area, bfs(r, c))
            
print(cnt)
print(max_area)