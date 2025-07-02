### 백준 16637: 괄호 추가하기

def operate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    if operator == '-':
        return num1 - num2
    if operator == '*':
        return num1 * num2

def dfs(index, total):
    global result
    if index >= N - 1:
        result = max(result, total)
        return
    
    next_total = operate(total, expression[index+1], expression[index+2])
    dfs(index+2, next_total)
    
    if index + 4 < N:
        temp = operate(expression[index+2], expression[index+3], expression[index+4])
        next_total = operate(total, expression[index+1], temp)
        dfs(index + 4, next_total)

N = int(input())
expression = list(input().strip())
expression = [int(expression[i]) if i % 2 == 0 else expression[i] for i in range(N)]

if N == 1: 
    print(expression[0])
    exit()
    
result = -int(1e9)
dfs(0, expression[0])
print(result)