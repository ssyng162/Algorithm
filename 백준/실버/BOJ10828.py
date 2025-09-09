### 백준 10828: 스택

import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    parts = input().strip().split()
    
    if parts[0] == 'push':
        stack.append(int(parts[1]))
    elif parts[0] == 'pop':
        print(stack.pop() if stack else -1)
    elif parts[0] == 'size':
        print(len(stack))
    elif parts[0] == 'empty':
        print(1 if not stack else 0)
    elif parts[0] == 'top':
        print(stack[-1] if stack else -1)