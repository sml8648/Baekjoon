from itertools import combinations
def check_minimize(keys, comb):

    for key in keys:
        tmp_count = 0
        for column in key:
            if column in comb:
                tmp_count +=1
        if tmp_count == len(key):
            return False
    return True

def solution(relation):

    num = len(relation[0])
    all_combs = []
    for i in range(1, num+1):
        tmp = list(combinations(range(num),i))
        all_combs.extend(tmp)

    result = []
    for comb in all_combs:
        tmp_set = set()
        for row in relation:
            distinct = []
            for idx in comb:
                try:
                    distinct.append(row[idx])
                except:
                    breakpoint()
            tmp_set.add(tuple(distinct))

        if len(tmp_set) == len(relation):
            if check_minimize(result, comb): result.append(comb)

    return len(result)