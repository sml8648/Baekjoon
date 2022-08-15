n = int(input())

for _ in range(n):

    a = int(input())
    tmp = a**2
    
    if str(tmp)[-len(str(a)):] == str(a):
        print('YES')
    else:
        print('NO')