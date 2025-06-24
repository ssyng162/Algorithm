### 프로그래머스: [PCCP 기출문제] 1번 / 동영상 재생기

def solution(video_len, pos, op_start, op_end, commands):
    for c in commands:
        pos=op_skip(pos, op_start, op_end)
        if(c=="next"):
            pos=next(pos, video_len)
            print("next, ", pos)
        if(c=="prev"):
            pos=prev(pos)
            print("prev, ", pos)
        pos=op_skip(pos, op_start, op_end)
    return pos

def op_skip(time, op_start, op_end):
    if(op_start<=time and time<=op_end):
        return op_end
    return time
    

def next(time, video_len):
    m=int(time[0:2])
    s=int(time[3:])+10
    
    if s>59:
        s-=60
        m+=1
        
    time=""
    if(m<10):
        time+="0"
        time+=str(m)
    else: 
        time+=str(m)
    time+=":"
    if(s<10):
        time+="0"
        time+=str(s)
    else: 
        time+=str(s)
    
    return min(time, video_len)
    
    
    
def prev(time):
    m=int(time[0:2])
    s=int(time[3:])-10
    
    if(s<0):
        s+=60
        m-=1
    
    if m<0: return "00:00"
    
    time=""
    if(m<10):
        time+="0"
        time+=str(m)
    else: 
        time+=str(m)
    time+=":"
    if(s<10):
        time+="0"
        time+=str(s)
    else: 
        time+=str(s)
    
    return time