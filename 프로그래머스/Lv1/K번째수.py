### 프로그래머스: K번째수

def solution(array, commands):
    answer = []
    for nums in commands:
        answer.append(calc(array, nums[0], nums[1], nums[2]))
    return answer

def calc(array, i, j, k):
    array=array[i-1:j]
    array.sort()
    
    return array[k-1]