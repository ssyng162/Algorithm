# 백준 1781: 컵라면

import sys
import heapq

input = sys.stdin.readline

problems = []
N = int(input())

for _ in range(N):
    deadline, ramen = map(int, input().split())
    problems.append((deadline, ramen))

problems.sort(key=lambda x: x[0])

heap = []

for deadline, ramen in problems:
    heapq.heappush(heap, ramen)
    if len(heap) > deadline:
        heapq.heappop(heap)

print(sum(heap))
