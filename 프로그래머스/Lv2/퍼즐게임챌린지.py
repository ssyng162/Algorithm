### 프로그래머스: [PCCP 기출문제] 2번 / 퍼즐 게임 챌린지

def solution(diffs, times, limit):
    def can_success(level):
        total_time = 0

        for i in range(len(diffs)):
            if(diffs[i] <= mid_level):
                total_time += times[i]
            else:
                total_time += (times[i]+times[i-1])*(diffs[i]-mid_level) + times[i]

            if total_time > limit: 
                return False

        return True
    
    
    min_level = 1
    max_level = 100000
    answer = 100000
    
    while(min_level <= max_level):
        mid_level = (min_level+max_level)//2
        
        if(can_success(mid_level)):
            answer = mid_level
            max_level = mid_level - 1
        else:
            min_level = mid_level + 1
    
    return answer