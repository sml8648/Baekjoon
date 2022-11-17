import sys
input = sys.stdin.readline

a = int(input())

n = 200001
a_list = [1]*n

for i in range(2, int(n**0.5) + 1):
    if a_list[i]:
        for j in range(2*i,n, i):
            a_list[j] = 0

count = -2

for idx,i in enumerate(a_list):
    
    if i == 1:
        count += 1
    
    if count == a:
        print(idx)
        break