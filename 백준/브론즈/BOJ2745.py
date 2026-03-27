# 백준 2745: 진법 변환

import sys
input = sys.stdin.readline

N, B = input().split()
B = int(B)

print(int(N, B))
