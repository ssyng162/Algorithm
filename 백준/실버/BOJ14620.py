### 백준 14620: 꽃길

from itertools import combinations

def calc_cost(com, cur_min):
    used = set()
    cost = 0

    for x, y in com:
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy

            if (nx, ny) in used:
                return float('inf')

            used.add((nx, ny))
            cost += flowerBed[nx][ny]
            if cost >= cur_min:
                return float('inf')

    return cost

        

N = int(input())
flowerBed = [list(map(int, input().split())) for _ in range(N)]
positions = [(i, j) for i in range(1, N-1) for j in range(1, N-1)]
combination = combinations(positions, 3)

#중심, 상하좌우
dirs = [(0,0), (-1,0), (1,0), (0,-1), (0,1)]

result = float('inf')

for com in combination:
    cost = calc_cost(com, result)
    result = min(result, cost)

print(result)