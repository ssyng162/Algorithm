### 백준 2579: 계단 오르기

import sys
input = sys.stdin.readline

n = int(input())
stair = [int(input()) for _ in range(n)]

if n == 1:
    print(stair[0])
    exit()
elif n == 2:
    print(stair[0] + stair[1])
    exit()
elif n == 3:
    print(max(stair[0] + stair[2], stair[1] + stair[2]))
    exit()

a = stair[0]
b = stair[0] + stair[1]
c = max(stair[0] + stair[2], stair[1] + stair[2])

for i in range(3, n):
    a, b, c = b, c, max(b + stair[i], a + stair[i-1] + stair[i])
    
print(c)