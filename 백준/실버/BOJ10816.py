# 백준 10816: 숫자 카드 2

import sys
input = sys.stdin.readline

N = int(input())
holding_cards = list(map(int, input().split()))
count = {}

for card in holding_cards:
    count[card] = count.get(card, 0) + 1

M = int(input())
target_cards = list(map(int, input().split()))

result = [str(count.get(card, 0)) for card in target_cards]
print(' '.join(result))
