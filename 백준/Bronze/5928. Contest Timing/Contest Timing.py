a,b,c = map(int,input().split())

import datetime

q = datetime.datetime(2011,11,a,b,c)
t = datetime.datetime(2011,11,11,11,11)

tmp = q - t

tmp_1 = tmp.total_seconds() / 60

if tmp_1 >= 0:
    print(int(tmp_1))
else:
    print(-1)