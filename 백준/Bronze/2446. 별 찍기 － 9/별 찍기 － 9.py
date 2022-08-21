N = int(input())

for i in range(N,1,-1):

    b = ' '*(N-i)+'*'*((2*i)-1)

    print(b)

for i in range(1,N+1):

    b = ' '*(N-i)+'*'*((2*i)-1)

    print(b)