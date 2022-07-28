import datetime

a = int(input())
b = int(input())

aa = datetime.datetime(2015,a,b)
tmp = datetime.datetime(2015,2,18)

if aa == tmp:
    print('Special')
elif aa > tmp:
    print('After')
else:
    print('Before')