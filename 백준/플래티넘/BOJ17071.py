### 백준 17071: 숨바꼭질 5

from collections import deque

def bfs(subin):
    queue = deque()
    queue.append((subin, 0))
    visited[0][subin] = 0
    
    while queue:
        x, t = queue.popleft()
        
        for nx in (x-1, x+1, x*2):
            if nx<0 or nx>500000 or visited[(t+1)%2][nx] != -1:
                continue
            queue.append((nx, t+1))
            visited[(t+1)%2][nx] = t+1
            
subin, sister = map(int, input().split())
visited = [[-1] * 500001 for _ in range(2)]
bfs(subin)

time = 0

while True:
    sister += time
    
    if sister > 500000:
        print(-1)
        break
    if visited[time%2][sister] != -1 and visited[time%2][sister] <= time:
        print(time)
        break
    time += 1