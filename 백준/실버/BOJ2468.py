### 백준 2468: 안전 영역

from collections import deque

#상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if not (0 <= nx < N and 0 <= ny < N): continue
            if visited[nx][ny] or area[nx][ny] <= rain: continue
        
            queue.append((nx, ny))
            visited[nx][ny] = True
    
    

    
N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
max_safe_zone = 0
max_height = max(map(max, area))

for rain in range(max_height+1):
    visited = [[False]*N for _ in range(N)]
    count = 0
    
    for i in range(N):
        for j in range(N):
            if area[i][j]>rain and visited[i][j]==False:
                count += 1
                bfs(i, j)
                
    max_safe_zone = max(max_safe_zone, count)

print(max_safe_zone)