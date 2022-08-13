def solution(n, arr1, arr2):
    answer = []
    
    for a,b in zip(arr1, arr2):
        

        a_bin = str(bin(a))[2:]
        if len(a_bin) != n:
            a_bin = '0'*(n - len(a_bin)) + a_bin

        b_bin = str(bin(b))[2:]
        if len(b_bin) != n:
            b_bin = '0'*(n - len(b_bin)) + b_bin
        
        tmp_answer = []
        print(a_bin, b_bin)
        

        for c,d in zip(a_bin, b_bin):
            
            if int(c) == 0 and int(d) == 0:
                tmp_answer.append(' ')
            else:
                tmp_answer.append('#')
        answer.append(''.join(tmp_answer))
        
    return answer