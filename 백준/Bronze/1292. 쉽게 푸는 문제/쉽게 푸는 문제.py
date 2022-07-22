import sys
input = sys.stdin.readline

a,b = map(int,input().split())
a_list = []

for i in range(46):
    for j in range(i+1):
        a_list.append(i+1)


print(sum(a_list[a-1:b]))