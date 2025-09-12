### 백준 9095: 1, 2, 3 더하기

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    
    dp1 = 1
    dp2 = 2
    dp3 = 4
    
    if n <= 3:
        print([0, dp1, dp2, dp3][n])
        continue
    
    for i in range(4, n+1):
        dp1, dp2, dp3 = dp2, dp3, dp1 + dp2 + dp3
    print(dp3)