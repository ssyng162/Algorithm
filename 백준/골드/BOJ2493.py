### 백준 2493: 탑

N = int(input())
tower_heights = list(map(int, input().split()))
stack = []
answer = []

for i in range(N):
    height = tower_heights[i]
    while stack and stack[-1][1] < height:
        stack.pop()
    answer.append(stack[-1][0] + 1 if stack else 0)
    stack.append((i, height))
    
print(*answer)