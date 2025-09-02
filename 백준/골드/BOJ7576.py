### 백준 7576: 토마토

from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    
    for r in range(row):
        for c in range(column):
            if tomatos[r][c] == 1:
                queue.append((r, c))
    
    while queue:
        cx, cy = queue.popleft()
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if not 0 <= nx < row or not 0 <= ny < column:
                continue
            if tomatos[nx][ny] != 0:
                continue
            
            tomatos[nx][ny] = tomatos[cx][cy] + 1
            queue.append((nx, ny))


column, row = map(int, input().split())
tomatos = [list(map(int, input().split())) for _ in range(row)]

bfs()

answer = 0
for r in range(row):
    if 0 in tomatos[r]: 
        print(-1)
        sys.exit()
    row_max = max(tomatos[r])
    answer = max(answer, row_max)
    
print(answer - 1)
