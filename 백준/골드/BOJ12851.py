### 백준 12851: 숨바꼭질 2

from collections import deque

def bfs(subin, sister):
    visited = [-1] *100001
    visited[subin] = 0
    queue = deque([subin])
    
    min_time = float('inf')
    cnt = 0
    
    while queue:
        x = queue.popleft()
        
        for nx in (x+1, x-1, x*2):
            
            if nx<0 or nx>100000: 
                continue
                
            if visited[nx] == -1:
                visited[nx] = visited[x] + 1
                queue.append(nx)
            elif visited[nx] == visited[x] + 1:
                queue.append(nx)
                
            if nx == sister:
                if visited[x] + 1 < min_time:
                    min_time = visited[x] + 1
                    cnt = 1
                elif visited[x] + 1 == min_time:
                    cnt += 1
    return min_time, cnt


subin, sister = map(int, input().split())

if subin == sister:
    print(0)
    print(1)
else:
    time, count = bfs(subin, sister)
    print(time)
    print(count)