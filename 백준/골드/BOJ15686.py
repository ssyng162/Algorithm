# 백준 15686: 치킨 배달

import sys
from itertools import combinations

input = sys.stdin.readline

def calc_chicken_dist(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

houses = []
chicken_stores = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chicken_stores.append((i, j))

min_city_chicken_dist = float('inf')

for combination in combinations(chicken_stores, M):
    total_city_dist = 0

    for house in houses:
        min_chicken_dist = float('inf')

        for chicken_store in combination:
            min_chicken_dist = min(
                min_chicken_dist,
                calc_chicken_dist(house, chicken_store)
            )

        total_city_dist += min_chicken_dist

        if total_city_dist > min_city_chicken_dist:
            break

    min_city_chicken_dist = min(min_city_chicken_dist, total_city_dist)

print(min_city_chicken_dist)
