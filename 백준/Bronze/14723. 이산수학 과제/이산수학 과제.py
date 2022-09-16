a = int(input())
tmp_2 = a
tmp_1 = -1
for i in range(1,1000):

    tmp_2 = tmp_2 - i

    if tmp_2 < 0:
        tmp_1 = i
        break

if abs(tmp_1) == abs(tmp_2):
    print(1, tmp_1 -1)
else:
    print(abs(tmp_2)+1,tmp_1 + tmp_2)