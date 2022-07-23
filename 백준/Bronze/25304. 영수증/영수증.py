import sys
input = sys.stdin.readline

a = int(input())
n = int(input())

sum = 0
for _ in range(n):
    c,d = map(int,input().split())
    
    sum += c*d
    
if sum == a:
    print('Yes')
else:
    print('No')