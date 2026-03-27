# 프로그래머스: 가장 큰 수

def solution(numbers):
    str_numbers = [str(num) for num in numbers]
    str_numbers.sort(reverse=True, key=lambda x: x*3)
    return str(int(''.join(str_numbers)))