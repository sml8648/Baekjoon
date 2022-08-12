def solution(A,B):
    answer = 0

    a_list = sorted(A)
    b_list = sorted(B,reverse=True)
    
    for a,b in zip(a_list,b_list):
        answer += a*b

    return answer