### 백준 10026: 적록색약

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def is_same_normal(c1, c2):
    return c1 == c2

def is_same_cb(c1, c2):
    if c1 == c2:
        return True
    return (c1 in "RG") and (c2 in "RG")

def bfs(x, y, visited, is_same):
    queue = deque([(x, y)])
    visited[x][y] = True
    color = picture[x][y]
    
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if not(0<=nx<N and 0<=ny<N):
                continue
            if visited[nx][ny]:
                continue
            if not is_same(picture[nx][ny], color):
                continue
            visited[nx][ny] = True
            queue.append((nx, ny))
    
    
N = int(input())
picture = [input().strip() for _ in range(N)]
visited_normal = [[False]*N for _ in range(N)]
visited_cb = [[False]*N for _ in range(N)]
cnt1 = 0
cnt2 = 0

for i in range(N):
    for j in range(N):
        if not visited_normal[i][j]:
            cnt1 += 1
            bfs(i, j, visited_normal, is_same_normal)
        if not visited_cb[i][j]:
            cnt2 += 1
            bfs(i, j, visited_cb, is_same_cb)

print(cnt1, cnt2)