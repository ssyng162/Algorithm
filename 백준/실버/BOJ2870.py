### 백준 2870: 수학숙제

N = int(input())
result = []

def find_num(s):
    num = []
    nums = []
    for c in s:
        if c.isdigit(): 
            num.append(c)
        else:
            if num:
                nums.append(int(''.join(num)))
                num = []
        
    if num:
        nums.append(int(''.join(num)))
    
    return nums
        

    
for _ in range(N):
    s = input()
    result.extend(find_num(s))

result.sort()
print(*result, sep="\n")
