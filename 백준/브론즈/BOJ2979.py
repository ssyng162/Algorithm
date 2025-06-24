### 백준 2979: 트럭 주차

A, B, C = map(int, input().split())

time = [0]*100

for _ in range(3):
    start, end = map(int, input().split())
    for i in range(start, end):
        time[i]+=1

total = 0
total+=time.count(1)*A*1
total+=time.count(2)*B*2
total+=time.count(3)*C*3

print(total)