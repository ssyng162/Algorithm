### 백준 2667: 단지번호 붙이기

from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    count = 1
    
    while queue:
        cx, cy = queue.popleft()
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if not(0<=nx<N and 0<=ny<N):
                continue 
            
            if matrix[nx][ny] == 0:
                continue
            
            if visited[nx][ny]:
                continue
            
            visited[nx][ny] = True
            count += 1
            queue.append((nx, ny))
            
    return count

N = int(input())
matrix = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

sizes = []

for i in range(N):
    for j in range(N):
        if visited[i][j]: 
            continue
        if matrix[i][j] == 0:
            continue
        sizes.append(bfs(i, j))
        
print(len(sizes))
sizes.sort()
for v in sizes:
    print(v)