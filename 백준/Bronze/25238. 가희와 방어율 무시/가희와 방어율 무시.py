import sys
input = sys.stdin.readline

a,b = map(int,input().split())

b = float(b/100)

result = a - (a*b)

if result >= 100:
    print(0)
else:
    print(1)