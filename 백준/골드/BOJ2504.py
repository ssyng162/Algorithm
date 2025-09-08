### 백준 2504: 괄호의 값

line = input()
stack = []

def opposite(cur):
    return '[' if cur == ')' else '('

def pair(cur):
    return '(' if cur == ')' else '['

def score(cur):
    return 2 if cur == ')' else 3

def calc_total(cur):
    total = 0
    while True:
        if not stack or stack[-1] == opposite(cur):
            return False
        if stack[-1] == pair(cur):
            stack.pop()
            break
        top = stack.pop()
        if isinstance(top, int):
            total += top
        else:
            return False        
    stack.append(max(total*score(cur), score(cur)))
    return True

is_possible = True

for l in line:
    if l == '(' or l=='[':
        stack.append(l)
    elif stack:
        if not calc_total(l):
            is_possible = False
            break
    else:
        is_possible = False
        break
    
answer = 0

while stack and is_possible:
    x = stack.pop()
    if not isinstance(x, int):
        is_possible = False
        break
    answer += x
    
print(answer if is_possible else 0)