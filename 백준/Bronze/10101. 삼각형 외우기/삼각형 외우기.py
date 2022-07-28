a = int(input())
b = int(input())
c = int(input())

sum = a+b+c

tmp_set = set()
tmp_set.add(a)
tmp_set.add(b)
tmp_set.add(c)

if sum == 180 and len(tmp_set) == 1:
    print('Equilateral')
elif sum == 180 and len(tmp_set) == 2:
    print('Isosceles')
elif sum == 180 and len(tmp_set) == 3:
    print('Scalene')
elif sum != 180:
    print('Error')
else:
    pass