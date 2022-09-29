while True:
    n = int(input())
    if n == -1:
        break

    before = 0
    sum = 0
    for i in range(n):
        a,b = map(int,input().split())
        b = b - before
        sum += (a*b)
        before += b

    print(sum,'miles')