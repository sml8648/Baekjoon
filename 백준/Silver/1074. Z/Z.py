import sys
input = sys.stdin.readline

N, r, c = map(int,input().split())

def Z(N,r,c,a_list):

    if N == 1:
        if r == 0 and c == 0:
            a_list.append(1)
        elif r == 0 and c == 1:
            a_list.append(2)
        elif r == 1 and c == 0:
            a_list.append(3)
        elif r == 1 and c == 1:
            a_list.append(4)

        return a_list
    else:

        one_share, one_remainder = divmod(r,2**(N-1))
        two_share, two_remainder = divmod(c,2**(N-1))

        multiplier = -1
        if one_share == 0 and two_share == 0:
            multiplier = 1
        elif one_share == 0 and two_share == 1:
            multiplier = 2
        elif one_share == 1 and two_share == 0:
            multiplier = 3
        elif one_share == 1 and two_share == 1:
            multiplier = 4

        a_list.append(multiplier)
        Z(N-1,one_remainder,two_remainder,a_list)
        return a_list

result = Z(N,r,c,[])

total = (2**N)**2

for i in range(N,0,-1):
    count = 4 - result[N-i]
    tmp = ((2**i)**2) // 4
    total -= count*tmp

print(total-1)