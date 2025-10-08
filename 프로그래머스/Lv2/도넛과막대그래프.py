### 프로그래머스: 2024 KAKAO WINTER INTERNSHIP / 도넛과 막대 그래프

from collections import defaultdict

INDEGREE = 0
OUTDEGREE = 1

def solution(edges):
    degree = defaultdict(lambda: [0, 0]) 
    
    for edge in edges:
        start, target = edge
        degree[start][OUTDEGREE] += 1
        degree[target][INDEGREE] += 1
        
    created_edge = 0
    bar_cnt = 0
    eight_cnt = 0
        
    for edge_number, value in degree.items():
        if value[INDEGREE] == 0  and value[OUTDEGREE] >= 2:
            created_edge = edge_number
        if value[OUTDEGREE] == 0:
            bar_cnt += 1
        if value[INDEGREE] >= 2 and value[OUTDEGREE] == 2:
            eight_cnt += 1
    donut_cnt = degree[created_edge][OUTDEGREE] - (bar_cnt + eight_cnt)
    
    return [created_edge, donut_cnt, bar_cnt, eight_cnt]