# 백준 1475: 방 번호

count = [0] * 10
for n in map(int, input()):
    count[n] += 1

count[6] = (count[6] + count[9] + 1)//2
print(max(count[:9]))
