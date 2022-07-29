import datetime


for _ in range(3):
    a1,b1,c1,d1,e1,f1 = map(int,input().split())

    tmp_1 = datetime.datetime(2000,1,1,a1,b1,c1)
    tmp_2 = datetime.datetime(2000,1,1,d1,e1,f1)

    result = str(tmp_2 - tmp_1)
    result = result.split(':')

    print(result[0],end=' ')

    if result[1][0] == '0':
        print(result[1][1:],end=' ')
    else:
        print(result[1],end=' ')

    if result[2][0] == '0':
        print(result[2][1:],end=' ')
    else:
        print(result[2],end=' ')
    print()