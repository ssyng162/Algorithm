### 백준 1874: 스택 수열

import sys

n = int(input())
A = [int(input()) for _ in range(n)]
cur = 1
answer = []
stack = []

for a in A:
    while(cur <= a):
        stack.append(cur)
        cur += 1
        answer.append("+")
        
    if stack[-1] == a:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        sys.exit()
        
print('\n'.join(answer))