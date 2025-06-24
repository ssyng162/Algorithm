### 백준 10709: 기상캐스터

H, W = map(int, input().split())

result = []

def calc_cloud_arrival_time(row):
    cloud = -1
    result = []
    for w in range(len(row)):
        if row[w] == 'c':
            cloud = w
            result.append(0)
        elif cloud != -1:
            result.append(w - cloud)
        else:
            result.append(-1)
    return result
                
        

for h in range(H):
    row = input()
    result.append(calc_cloud_arrival_time(row))

for line in result:
    print(*line)