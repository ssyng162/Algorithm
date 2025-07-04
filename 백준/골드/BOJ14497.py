### 백준 14497: 주난의 난

from collections import deque

#상하좌우
dx = [-1, 1, 0, 0] #상하
dy = [0, 0, -1, 1] #좌우

def bfs(jx, jy):
    queue = deque()
    visited[jx][jy] = 0
    queue.append((jx, jy))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not 0<=nx<row or not 0<=ny<column:
                continue
            if visited[nx][ny] != -1:
                continue
            if classroom[nx][ny] in ('1', '#'):
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
            else:
                visited[nx][ny] = visited[x][y]
                queue.appendleft((nx, ny))
                
row, column = map(int, input().split())
jx, jy, tx, ty = map(lambda x: int(x) -1, input().split())
classroom = [list(input().strip()) for _ in range(row)]
visited = [[-1] * column for _ in range(row)]
bfs(jx, jy)
print(visited[tx][ty])