# 백준 1967: 트리의 지름

from collections import deque
import sys
input = sys.stdin.readline
        
def bfs(start, graph, n):
    dist = [-1] * (n+1)
    dist[start] = 0
    queue = deque([start])
    
    farthest_node = start
    farthest_dist = 0
    
    while queue:
        cur = queue.popleft()
        
        for nxt, cost in graph[cur]:
            if dist[nxt] != -1:
                continue
            dist[nxt] = dist[cur] + cost
            queue.append(nxt)
            
            if dist[nxt] > farthest_dist:
                farthest_dist = dist[nxt]
                farthest_node = nxt
    return farthest_node, farthest_dist
    
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    cur, nxt, cost = map(int, input().split())
    graph[cur].append((nxt, cost))
    graph[nxt].append((cur, cost))
    
node, _ = bfs(1, graph, n)
_, answer = bfs(node, graph, n)
print(answer)
