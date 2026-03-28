# 백준 2206: 벽 부수고 이동하기

from collections import deque
import sys

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())

queue = deque()
queue.append((0, 0, 0))
grid = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

while queue:
    cx, cy, is_broken = queue.popleft()
    if cx == N - 1 and cy == M - 1:
        print(visited[cx][cy][is_broken])
        sys.exit()

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]

        if not (0 <= nx < N and 0 <= ny < M):
            continue

        if grid[nx][ny] == 1:
            if is_broken or visited[nx][ny][1] != 0:
                continue
            visited[nx][ny][1] = visited[cx][cy][is_broken] + 1
            queue.append((nx, ny, 1))
            continue

        if grid[nx][ny] == 0 and visited[nx][ny][is_broken] == 0:
            visited[nx][ny][is_broken] = visited[cx][cy][is_broken] + 1
            queue.append((nx, ny, is_broken))

print(-1)
