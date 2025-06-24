### 백준 1012: 유기농 배추

from collections import deque

def bfs(start_y, start_x):
    queue = deque([(start_y, start_x)])
                
    while queue:
        y, x = queue.popleft()
                    
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
                    
            if nx>=0 and ny>=0 and nx<M and ny<N and farm[ny][nx]==1:
                    farm[ny][nx] = 0
                    queue.append((ny, nx))

                    
T = int(input())

#상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(T):
    M, N, K = map(int, input().split())
    farm = [[0]*M for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1
    
    count = 0
    
    for i in range(N):
        for j in range(M):
            if farm[i][j]==1:
                farm[i][j] = 0
                count += 1
                bfs(i, j)

    print(count)               