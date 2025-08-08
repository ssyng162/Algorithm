### 백준 17471: 게리맨더링

from collections import deque

def is_valid(group):
    queue = deque([group[0]])
    visited = [False] * (N)
    visited[group[0]] = True
    cnt = 1
    
    while queue:
        cur = queue.popleft()
        for neighbor in adj[cur]:
            if neighbor in group and not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                cnt += 1
    return cnt == len(group)

N = int(input())
population = list(map(int, input().split()))
adj = [[] for _ in range(N)]

for i in range(N):
    line = list(map(int, input().split()))
    for neighbor in line[1:]:
        adj[i].append(neighbor-1)

result = float('inf')

for i in range(1, (1 << N) // 2 + 1):
    g1 = []
    g2 = []
        
    for j in range(N):
        if (i>>j) & 1:
            g1.append(j)
        else:
            g2.append(j)
    
    if is_valid(g1) and is_valid(g2):
        g1_population = sum(population[i] for i in g1)
        g2_population = sum(population[i] for i in g2)
        difference = abs(g1_population - g2_population)
        result = min(result, difference)
        
print(result if result != float('inf') else -1)