### 백준 3197: 백조의 호수

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    visited = [[-1]*column for _ in range(row)]
    queue = deque()
    
    for i in range(row):
        for j in range(column):
            if lake[i][j] in ('.', 'L'):
                visited[i][j] = 0
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<row and 0<=ny<column and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                
    return visited
                
def can_meet(day, melted_day):
    visited = [[False]*column for _ in range(row)]
    queue = deque()
    
    queue.append(swan[0])
    visited[swan[0][0]][swan[0][1]] = True

    while queue:
        x, y = queue.popleft()
        if (x, y) == swan[1]:
            return True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < column:
                if not visited[nx][ny] and melted_day[nx][ny] <= day:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return False

row, column = map(int, input().split())
lake = [list(input().strip()) for _ in range(row)]

swan = []
for i in range(row):
    for j in range(column):
        if lake[i][j] == 'L':
            swan.append((i, j))

melted_day = bfs()
            
left = 0
right = max(max(row) for row in melted_day)

result = 0

while left <= right:
    mid = (left + right) //2
    if can_meet(mid, melted_day):
        result = mid
        right = mid - 1
    else:
        left = mid + 1

print(result)