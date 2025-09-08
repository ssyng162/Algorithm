### 백준 7569: 토마토

from collections import deque
import sys
input = sys.stdin.readline

#상하좌우 위 아래
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    queue = deque()
    
    for h in range(height):
        box = []
        for r in range(row):
            row_tomatos = list(map(int, input().split()))
            
            for c in range(column):
                if row_tomatos[c] == 1:
                    queue.append((r, c, h))
            box.append(row_tomatos)
        tomatos.append(box)
    
    while queue:
        cx, cy, cz = queue.popleft()
        
        for i in range(6):
            nx = cx + dx[i]
            ny = cy + dy[i]
            nz = cz + dz[i]
            
            if not(0<=nx<row and 0<=ny<column and 0<=nz<height):
                continue
            if tomatos[nz][nx][ny] != 0:
                continue
            
            tomatos[nz][nx][ny] = tomatos[cz][cx][cy] + 1
            queue.append((nx, ny, nz))
            
column, row, height = map(int, input().split())
tomatos = []

bfs()

answer = 0
for h in range(height):
    for r in range(row):
        if 0 in tomatos[h][r]:
            print(-1)
            sys.exit()
        row_max = max(tomatos[h][r])
        answer = max(answer, row_max)
        
print(answer - 1)