def convert(n, q):
    a_list = ['A','B','C','D','E','F']
    if n == 0:
        return '0'
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        if mod >= 10:
            rev_base += a_list[mod-10]
        else:
            rev_base += str(mod)
    return rev_base[::-1]


def solution(n, t, m, p):
    answer = ''
    
    for i in range(t*m):
        answer += convert(i,n)
        if len(answer) >= t*m:
            break
            
    
    final_result = ''
    for i in range(p-1,len(answer)+1,m):
        
        if len(final_result) == t:
            break
        try:
            final_result += answer[i]
        except:
            break

    return final_result