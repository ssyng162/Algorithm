### 백준 9012: 괄호

T = int(input())

for _ in range(T):
    PS = input()
    stack = []
    is_valid = True
    
    for ps in PS:
        if ps == '(': stack.append(ps)
        else:
            if stack: 
                stack.pop()
            else: 
                is_valid = False
                break
        
    if not stack and is_valid: print("YES")
    else: print("NO")
        