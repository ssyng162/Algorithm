### 백준 16234: 인구 이동

from collections import deque

size, minimum, maximum = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(size)]

#상하좌우
dx = [-1, 1, 0, 0] #상하
dy = [0, 0, -1, 1] #좌우

def bfs(x, y, index):
    queue = deque()
    queue.append((x, y))
    union = [(x, y)]
    union_sum = country[x][y]
    visited[x][y] = index
    
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if not 0<=nx<size or not 0<=ny<size:
                continue
            if visited[nx][ny]!=0:
                continue
            if not minimum <= abs(country[cx][cy] - country[nx][ny]) <= maximum:
                continue
            queue.append((nx, ny))
            visited[nx][ny] = index
            union.append((nx, ny))
            union_sum += country[nx][ny]
    population = union_sum // len(union)
    for ux, uy in union:
        country[ux][uy] = population
    return len(union)

result = 0
while True:
    visited = [[0]*size for _ in range(size)]
    index = 1
    moved = False
    
    for i in range(size):
        for j in range(size):
            if visited[i][j] ==0:
                if bfs(i, j, index) > 1:
                    moved = True
                index += 1
    if not moved:
        break
    result += 1

print(result)