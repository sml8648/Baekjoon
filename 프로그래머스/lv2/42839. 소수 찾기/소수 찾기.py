from itertools import permutations
def solution(numbers):
    tmp_set = set()
    for i in range(1,len(numbers)+1):
        tmp = permutations(numbers,i)
        for each in tmp:
            tmp_result = ''.join(each)
            tmp_set.add(int(tmp_result))


    D = [1]*(max(tmp_set) + 1)
    D[0], D[1] = 0, 0
    mv = max(tmp_set)
    for i in range(2,int(mv**(1/2))+1):
        if D[i]:
            for j in range(2*i,mv+1,i):
                D[j] = 0

    count = 0
    for i in tmp_set:
        if D[i]:
            count += 1
    return count