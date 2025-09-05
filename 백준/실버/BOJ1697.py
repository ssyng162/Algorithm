### 백준 1697: 숨바꼭질

from collections import deque

def bfs(start, end):
    visited = [-1]*100001
    queue = deque()
    
    visited[start] = 0
    queue.append(start)
    
    while queue:
        cur_pos = queue.popleft()
        
        if cur_pos == end:
            return visited[cur_pos]
        
        for next_pos in (cur_pos - 1, cur_pos + 1, 2 * cur_pos):
            if not 0<=next_pos<=100000:
                continue
            if visited[next_pos]!=-1:
                continue
            
            visited[next_pos] = visited[cur_pos] + 1
            queue.append(next_pos)
            
        
N, K = map(int, input().split())
print(bfs(N, K))