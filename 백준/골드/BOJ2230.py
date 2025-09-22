### 백준 2230: 수 고르기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

if M == 0:
    print(0)
    exit()

A = [int(input()) for _ in range(N)]
A.sort()

left = 0
right = 1
result = float('inf')

while left < N and right < N:
    if left == right:
        right += 1
        continue
        
    diff = A[right] - A[left]
    
    if diff < M:
        right += 1
    else:
        result = min(result, diff)
        left += 1

print(result)