import sys
input = sys.stdin.readline
from itertools import combinations

n,m = map(int,input().split())

x = set()
y = set()
a_list = list(map(str,input().split()))
a_list.sort()

for j in a_list:
    if j in ['a','e','i','o','u']:
        x.add(j)
    else:
        y.add(j)

b_list = [i for i in range(m)]

com_list = list(combinations(b_list,n))

for each in com_list:
    x_count = 0
    y_count = 0
    each_row = []
    for k in each:
        if a_list[k] in x:
            x_count += 1
        else:
            y_count += 1

        each_row.append(k)

    if x_count >= 1 and y_count >= 2:
        for q in each_row:
            print(a_list[q],end='')
        print()