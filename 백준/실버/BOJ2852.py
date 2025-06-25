### 백준 2852: NBA 농구

N = int(input())
score = [0, 0]
lead_time = [0, 0]
last_time = 0

def format_time(time):
    return f'{time // 60:02d}:{time % 60:02d}'

for _ in range(N):
    team, cur_time = input().split()
    team = int(team) - 1
    cur_time  = int(cur_time[:2])*60 + int(cur_time[3:])
    
    if score[0] > score[1]:
        lead_time[0] += cur_time - last_time
    elif score[1] > score[0]:
        lead_time[1] += cur_time - last_time
    
    score[team] += 1
    last_time = cur_time

if score[0] > score[1]:
        lead_time[0] += 48*60 - last_time
elif score[1] > score[0]:
        lead_time[1] += 48*60 - last_time
        
print(format_time(lead_time[0]))
print(format_time(lead_time[1]))