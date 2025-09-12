### 백준 1149: RGB 거리

import sys
input = sys.stdin.readline

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

R, G, B = cost[0]

for i in range(1, N):
    r, g, b = cost[i]
    R, G, B = r + min(G, B), g + min(R, B), b + min(R, G)
    
print(min(R, G, B))