### 백준 2309: 일곱 난쟁이

from itertools import combinations

h = [int(input()) for _ in range(9)]
for com in combinations(h, 7):
    if sum(com) == 100:
        for i in sorted(com):
            print(i)
        break