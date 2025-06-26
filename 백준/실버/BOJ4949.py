### 백준 4949: 균형잡힌 세상

def is_balanced(s):    
    stack = []
    for c in s:
        if c=='(' or c=='[': 
            stack.append(c)
        elif c==')':
            if stack and stack[-1] == '(':
                stack.pop()
            else: 
                return False
        elif c==']':
            if stack and stack[-1] == '[':
                stack.pop()
            else: 
                return False
    return not stack

while True:
    s = input()
    if s=='.': 
        break
    if is_balanced(s): 
        print("yes")
    else: 
        print("no")