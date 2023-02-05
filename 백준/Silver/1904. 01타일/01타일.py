
n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    a = 1
    b = 2

    for i in range(3,n+1):
        c = (b+a)%15746

        if i != n:
            a = b
            b = c

    print(c)