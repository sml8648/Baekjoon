a = str(input().strip())

tmp = len(a) // 10
for i in range(tmp+1):
    qq = 10*i
    tt = qq + 10
    print(a[qq:tt])