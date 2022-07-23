import sys
input = sys.stdin.readline

a = int(input())

for _ in range(a):
    
    tmp = str(input().strip())
    
    if 6 <= len(tmp) <= 9:
        print('yes')
    else:
        print('no')