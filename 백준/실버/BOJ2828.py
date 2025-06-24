### 백준 2828: 사과 담기 게임

def move_to(current, apple):
    if current<=apple<=current+M-1: return current
    
    if apple < current: return apple
    
    if current+M-1 < apple: return apple-M+1



N, M = map(int, input().split())
J = int(input())
current = 1
moves = 0

for _ in range(J):
    apple = int(input())
    next_point = move_to(current, apple)
    moves += abs(next_point - current)
    current = next_point

print(moves)
