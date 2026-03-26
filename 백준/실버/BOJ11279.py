# 백준 11279: 최대 힙

import heapq
import sys

input = sys.stdin.readline

max_heap = []
n = int(input())

for _ in range(n):
    x = int(input())
    if x == 0:
        print(-heapq.heappop(max_heap) if max_heap else 0)
    else:
        heapq.heappush(max_heap, -x)
