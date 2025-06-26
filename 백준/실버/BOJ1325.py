### 백준 1325: 효율적인 해킹

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(start):
    visited = [False] * (n+1)
    queue = deque([start])
    visited[start] = True
    count = 1
    
    while queue:
        current_node = queue.popleft()
        for next_node in graph[current_node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
                count += 1
    return count

maximum = -1
result = []

for i in range(1, n+1):
    hacked = bfs(i)
    if hacked > maximum:
        maximum = hacked
        result = [i]
    elif hacked == maximum:
        result.append(i)
        
print(*result)