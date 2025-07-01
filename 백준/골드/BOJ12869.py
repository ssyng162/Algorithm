### 백준 12869: 뮤탈리스크

from collections import deque

N = int(input())
scv = list(map(int, input().split()))
scv += [0] * (3 - len(scv))
    
visited = [[[False]*61 for _ in range(61)] for _ in range(61)]

damage = [
    (9, 3, 1),
    (9, 1, 3),
    (3, 9, 1),
    (3, 1, 9),
    (1, 9, 3),
    (1, 3, 9)
]

a, b, c = scv
queue = deque([(a, b, c, 0)])
visited[a][b][c] = True

while queue:
    a, b, c, cnt = queue.popleft()
    
    if a<=0 and b<=0 and c<=0:
        print(cnt)
        break
    
    for d in damage:
        na = max(0, a - d[0])
        nb = max(0, b - d[1])
        nc = max(0, c - d[2])
        
        if not visited[na][nb][nc]:
            visited[na][nb][nc] = True
            queue.append((na, nb, nc, cnt + 1))