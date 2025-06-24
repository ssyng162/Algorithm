### 백준 1940: 주몽

N = int(input())
M = int(input())

nums = list(map(int, input().split()))
nums.sort()

left = 0
right = N-1
total = 0

while left<right:
    s = nums[left]+nums[right]
    if(s>M):
        right-=1
    elif(s<M):
        left+=1
    elif(s==M):
        total+=1
        left+=1
        right-=1
        
print(total)