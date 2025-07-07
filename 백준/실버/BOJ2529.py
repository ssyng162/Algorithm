### 백준 2529: 부등호

k = int(input())
signs = input().split()

used = [False] * 10
answer = []

def is_valid(num1, op, num2):
    return num1 > num2 if op == '>' else num1 < num2

def dfs(dept, path):
    if dept == k + 1:
        answer.append(path)
        return
    
    for i in range(10):
        if not used[i]: 
            if dept == 0 or is_valid(int(path[-1]), signs[dept-1], i):
                used[i] = True
                dfs(dept + 1, path + str(i))
                used[i] = False
                
dfs(0, "")
answer.sort()
print(answer[-1])
print(answer[0])