### 프로그래머스: [PCCP 기출 문제]1번 / 붕대 감기

def solution(bandage, health, attacks):
    cur_health = health
    streak = 0
    cur_attack_idx = 0
    
    for i in range(attacks[-1][0] + 1):
        
        if attacks[cur_attack_idx][0] == i:
            streak = 0
            cur_health -= attacks[cur_attack_idx][1]
            
            if cur_health <= 0:
                return -1
            
            cur_attack_idx += 1
            
            continue        
            
        cur_health = min(health, cur_health + bandage[1])
        streak += 1
        
        if streak == bandage[0]:
            cur_health = min(health, cur_health + bandage[2])
            streak = 0
        
    return cur_health