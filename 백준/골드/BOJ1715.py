# 백준 1715: 카드 정렬하기

import heapq, sys
input = sys.stdin.readline

N = int(input())
cards = []

for _ in range(N):
    cards.append(int(input()))

heapq.heapify(cards)
total = 0

while len(cards) > 1:
    tmp = heapq.heappop(cards) + heapq.heappop(cards)
    total += tmp
    heapq.heappush(cards, tmp)
    
print(total)
