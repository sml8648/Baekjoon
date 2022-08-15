def solution(n):
    D = [0] * (n + 1)
    D[0] = 1
    D[2] = 3

    for i in range(4, n + 1, 2):
        tmp = 0
        for j in range(i, -1, -2):

            if i - 2 == j:
                tmp += (D[j]*3)%1000000007
            else:
                tmp += (D[j]*2)%1000000007
                
        D[i] = tmp%1000000007

    return int(D[n])