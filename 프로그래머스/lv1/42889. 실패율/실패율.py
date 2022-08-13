from collections import defaultdict

def solution(N, stages):
    answer = []
    d = defaultdict(object)
    d = defaultdict(lambda : 0)
    
    for each in stages:
        d[each] += 1
    
    new_d = dict()
    for i in range(N):
        new_d[i+1] = 0
    
    total_len = len(stages)
    for each in sorted(d):
        if each > N:
            continue
        new_d[each] = d[each] / total_len
        total_len -= d[each]
    
    final = {k:v for k, v in sorted(new_d.items(), key=lambda item: item[1],reverse=True)}
    
    answer = list(final.keys())
    return answer