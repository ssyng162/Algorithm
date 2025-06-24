### 백준 2583: 영역 구하기

from collections import deque

#상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    grid[y][x] = 1
    area = 1
    
    while queue:
        cx, cy = queue.popleft()
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if not (0<=nx<N and 0<=ny<M): continue
            if grid[ny][nx]==1: continue
                
            queue.append((nx, ny))
            grid[ny][nx] = 1
            area += 1
    
    return area



M, N, K = map(int, input().split())
grid = [[0]*N for _ in range(M)]

for _ in range(K):
    lbx, lby, rux, ruy = map(int, input().split())
    for x in range(lbx, rux):
        for y in range(lby, ruy):
            grid[y][x] = 1

count = 0
areas = []

for y in range(M):
    for x in range(N):
        if grid[y][x] == 0:
            count += 1
            areas.append(bfs(x, y))

areas.sort()
print(count)
print(*areas)