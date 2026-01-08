### 프로그래머스: 리코쳇 로봇

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(board, x, y, dir):    
    while True:
        nx, ny = x + dx[dir], y + dy[dir]
        
        if not(0<=nx<len(board) and 0<=ny<len(board[0])):
            return x, y
        
        if board[nx][ny] == "D":
            return x, y
        
        x = nx
        y = ny

def solution(board):
    x, y = 0, 0
    H, W = len(board), len(board[0])
    
    for i in range(H):
        for j in range(W):
            if board[i][j] == "R":
                x, y = i, j
    
    visited = [[-1] * W for _ in range(H)]
    queue = deque()
    
    visited[x][y] = 0
    queue.append((x, y))
    
    while queue:
        cx, cy = queue.popleft()
        
        for d in range(4):
            nx, ny = move(board, cx, cy, d)
            
            if board[nx][ny] == "G":
                return visited[cx][cy] + 1
            if nx == cx and ny == cy:
                continue
            if visited[nx][ny] != -1:
                continue
            
            visited[nx][ny] = visited[cx][cy] + 1
            queue.append((nx, ny))
            
    return -1