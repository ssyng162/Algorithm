### 백준 9996: 한국이 그리울 땐 서버에 접속하지

def is_match(pattern, s):
    start, end = pattern.split("*")
    
    if len(s) < len(start)+len(end):
        return False
    if not s.startswith(start):
        return False
    if not s.endswith(end):
        return False
    return True


N = int(input())
pattern = input()

for _ in range(N):
    s = input()
    
    if is_match(pattern, s): 
        print("DA")
    else:
        print("NE")