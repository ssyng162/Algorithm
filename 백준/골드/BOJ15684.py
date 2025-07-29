### 백준 15684: 사다리 조작

def is_match():
    for i in range(1, N+1):
        line = i
        for j in range(1, H+1):
            if ladder[j][line]:
                line += 1
            elif ladder[j][line-1]:
                line -= 1
        if line != i:
            return False
    return True

def dfs(cnt, ch, cn):
    global ans
    if is_match():
        ans = min(ans, cnt)
        return
    if cnt ==3 or ans <= cnt:
        return
    
    for i in range(ch, H+1):
        k=cn if i==ch else 1
        for j in range(k, N):
            if not ladder[i][j] and not ladder[i][j-1] and not ladder[i][j+1]:
                ladder[i][j]=True
                dfs(cnt+1, i, j)
                ladder[i][j]=False

N, M, H = map(int, input().split())
ladder = [[False] * (N+1) for _ in range(H+1)]

for _ in range(M):
    a, b = map(int, input().split())
    ladder[a][b] = True
    
ans = 4

dfs(0, 1, 1)
print(ans if ans<=3 else -1)