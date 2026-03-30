# 백준 2941: 크로아티아 알파벳

croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
s = input()

for c in croatia:
    s = s.replace(c, "*")

print(len(s))
