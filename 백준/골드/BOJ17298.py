### 백준 17298: 오큰수

N = int(input())
nums = list(map(int, input().split()))
result = [-1]*N
stack = []

for i in range(N-1, -1, -1):
    while stack and stack[-1] <= nums[i]:
        stack.pop()
    if stack:
        result[i] = stack[-1]
    stack.append(nums[i])
    
print(*result)