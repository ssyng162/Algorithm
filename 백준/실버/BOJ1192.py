### 백준 1192: 쿼드 트리

import sys
sys.setrecursionlimit(10**6)

def compress_video(part):
    if max(map(max, part)) == 0:
        return "0"
    if min(map(min, part)) == 1:
        return "1"
    else:
        mid = len(part)//2
        lu = compress_video([row[:mid] for row in part[:mid]])
        ru = compress_video([row[mid:] for row in part[:mid]])
        ld = compress_video([row[:mid] for row in part[mid:]])
        rd = compress_video([row[mid:] for row in part[mid:]])
        return f"({lu}{ru}{ld}{rd})"
        

N = int(input())
video = [list(map(int, input().strip())) for _ in range(N)]
print(compress_video(video))