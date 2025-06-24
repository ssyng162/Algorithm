### 백준 1620: 나는야 포켓몬 마스터 이다솜

N, M = map(int, input().split())

poketmons = {}

for i in range(1, N+1):
    name = input()
    poketmons[name] = i
    poketmons[str(i)] = name

for _ in range(M):
    print(poketmons[input()])