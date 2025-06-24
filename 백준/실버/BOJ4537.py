### 백준 4537: 1

while True:
    try:
        n = int(input())
    except EOFError:
        break
    
    num = 1
    length = 1
    
    while(True):
        if num % n == 0:
            print(length)
            break
        num = (num * 10 + 1 ) % n
        length += 1