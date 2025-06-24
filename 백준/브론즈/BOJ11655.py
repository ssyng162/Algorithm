### 백준 11655: ROT13

S = input()
result = []

for s in S:
    if(s.isalpha()):
        if s.isupper():
            result.append(chr((ord(s) - ord('A') + 13) % 26 + ord('A')))
        else:
            result.append(chr((ord(s) - ord('a') + 13) % 26 + ord('a')))
    else:
        result.append(s)
        
print("".join(result))