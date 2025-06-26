### 백준 14502: 연구소

from itertools import combinations
from collections import deque

#N(세로)*M(가로)
#빈칸 0, 벽 1, 바이러스 2
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

#상하좌우
dx = [0, 0, -1, 1] #좌우
dy = [-1, 1, 0, 0] #상하

empty = []
virus = []

for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            empty.append((i, j))
        elif lab[i][j] == 2:
            virus.append((i, j))

def spread_virus(tmp_lab):
    queue = deque(virus)
    while queue:
        y, x = queue.popleft()        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]         
            if 0 <= ny < N and 0 <= nx < M and tmp_lab[ny][nx] == 0:
                tmp_lab[ny][nx] = 2
                queue.append((ny, nx))

#안전 구역 개수를 찾느다
def simulate(walls):
    tmp_lab = [row[:] for row in lab]
    for y, x in walls:
        tmp_lab[y][x] = 1
    #바이러스 확산시를 반영
    spread_virus(tmp_lab)
    #안전구역 개수를 찾아 최댓값에 반영
    return sum(row.count(0) for row in tmp_lab)


result = 0
for walls in combinations(empty, 3):
    result = max(result, simulate(walls))
print(result)
    