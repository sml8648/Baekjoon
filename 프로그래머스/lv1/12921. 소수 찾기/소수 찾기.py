def solution(n):
    a_list = [1]*(n+1)

    a_list = [1]*1000001

    for i in range(2, int(1000001**0.5) + 1):
        if a_list[i]:
            for j in range(2*i,1000001, i):
                a_list[j] = 0
                
    return sum(a_list[:n+1]) - 2