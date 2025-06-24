### 백준 11650: 좌표 정렬하기

import sys

N = int(sys.stdin.readline())
matrix = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
matrix.sort()

for row in matrix:
    print(*row)