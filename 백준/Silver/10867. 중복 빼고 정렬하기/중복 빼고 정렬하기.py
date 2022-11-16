import sys
input = sys.stdin.readline

a = int(input())
a_list = set(list(map(int,input().split())))
a_list = list(a_list)
a_list.sort()

for each in a_list:
    print(each,end=' ')