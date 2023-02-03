import sys
input = sys.stdin.readline

n = int(input())
a_list = list(map(int,input().split()))
a_list.sort()

tmp = 1
for each in a_list:
    if tmp < each:
        break
       
    tmp += each
 
print(tmp)