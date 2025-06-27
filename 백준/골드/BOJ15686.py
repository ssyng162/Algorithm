### 백준 15686: 치킨 배달

from itertools import combinations

city_size, rest_store = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(city_size)]

houses = []
store = []

for i in range(city_size):
    for j in range(city_size):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            store.append((i, j))

result = 5000*13

for com in combinations(store, rest_store):
    min_city_dist = 0
    for house in houses:
        min_house_dist = 5000
        for c in com: 
            min_house_dist = min(min_house_dist, abs(house[0]-c[0])+abs(house[1]-c[1]))
        min_city_dist += min_house_dist
    result = min(result, min_city_dist)

print(result)
            