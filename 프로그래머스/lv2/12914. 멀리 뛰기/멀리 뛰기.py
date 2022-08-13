def solution(n):
    if n == 1:
        return 1
    D = [0]*(n+1)
    D[1] = 1
    D[2] = 2
    for i in range(3,n+1):
        
        D[i] = (D[i-1]+D[i-2])%1234567
        
    return D[n]