### 백준 1920: 수 찾기

#이분탐색
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

A.sort()

for num in nums:
    is_exist = False
    start = 0
    end = N - 1
    
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == num:
            is_exist = True
            break
        elif A[mid] < num:
            start = mid + 1
        elif A[mid] > num:
            end = mid - 1
    print(1 if is_exist else 0)

#set 사용
#set으로 풀기

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

A = set(A)

for num in nums:
    print(1 if num in A else 0)