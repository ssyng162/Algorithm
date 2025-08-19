### 백준 15926: 현욱은 괄호왕이야!!

n = int(input())
parentheses = input().strip()
stack = [-1]
answer = 0

for i, p in enumerate(parentheses):
    if p == '(':
        stack.append(i)
    else:
        if stack:
            stack.pop()
        if not stack:
            stack.append(i)
        else:
            answer = max(answer, i - stack[-1])

print(answer)