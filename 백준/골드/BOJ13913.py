### 백준 13913: 숨바꼭질 4

from collections import deque

def bfs(subin, sister):
    visited = [-1] * 100001
    visited[subin] = 0
    
    prev = [-1] * 100001
    
    queue = deque()
    queue.append(subin)
    
    while queue:
        x = queue.popleft()
        
        if x == sister:
            break
        
        for nx in (x-1, x+1, 2*x):
            if 0 <= nx <= 100000 and visited[nx] == -1:
                visited[nx] = visited[x] + 1
                prev[nx] = x
                queue.append(nx)
                
    path = []
    cur = sister
    while cur != -1:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    
    return visited[sister], path

subin, sister = map(int, input().split())  
time, order = bfs(subin, sister)
print(time)
print(*order)