### 백준 1189: 컴백홈

def dfs(x, y, dist):
    global answer
    
    if (x, y) == (0, column-1):
        if dist == k:
            answer += 1
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if not 0<=nx<row or not 0<=ny<column:
            continue
        if visited[nx][ny] or graph[nx][ny]=='T':
            continue
        
        visited[nx][ny] = True
        dfs(nx, ny, dist+1)
        visited[nx][ny] = False

row, column, k = map(int, input().split())
graph = [list(input().strip()) for _ in range(row)]
visited = [[False]*column for _ in range(row)]
visited[row-1][0] = True

#상하좌우
dx = [-1, 1, 0, 0] #상하
dy = [0, 0, -1, 1] #좌우

answer = 0

dfs(row-1, 0, 1)
print(answer)