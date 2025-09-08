### 백준 7562: 나이트의 이동

from collections import deque

move = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, -1), (2, 1), (1, -2), (1, 2)]

def bfs(length, sx, sy, ex, ey):
    queue = deque()
    visited = [[-1]*length for _ in range(length)]
    visited[sx][sy] = 0
    queue.append((sx, sy))
    
    while queue:
        x, y = queue.popleft()
        
        if x == ex and y == ey:
            return visited[x][y]
        
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            
            if not(0<=nx<length and 0<=ny<length):
                continue
            if visited[nx][ny] != -1:
                continue
            
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))

testcase = int(input())

for _ in range(testcase):
    length = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    
    print(bfs(length, sx, sy, ex, ey))