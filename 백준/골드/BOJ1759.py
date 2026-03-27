# 백준 1759: 암호 만들기

import sys
from itertools import combinations
input = sys.stdin.readline

L, C = map(int, input().split())
chars = sorted(input().split())
vowels = {'a', 'e', 'i', 'o', 'u'}

for word in combinations(chars, L):
    vowel_count = sum(1 for ch in word if ch in vowels)
    consonant_count = L - vowel_count

    if vowel_count >= 1 and consonant_count >= 2:
        print(''.join(word))