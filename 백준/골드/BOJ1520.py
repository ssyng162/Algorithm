# 백준 1520: 내리막 길

import sys
sys.setrecursionlimit(10**6)

r, c = map(int, input().split())
sites = [list(map(int, input().split())) for _ in range(r)]

# dp[r][c] = (r, c)에서 도착점까지 가는 경우의 수
dp = [[-1] * c for _ in range(r)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y):
    if (x, y) == (r - 1, c - 1):
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if not (0 <= nx < r and 0 <= ny < c):
            continue
        if sites[nx][ny] >= sites[x][y]:
            continue
        dp[x][y] += dfs(nx, ny)

    return dp[x][y]

print(dfs(0, 0))