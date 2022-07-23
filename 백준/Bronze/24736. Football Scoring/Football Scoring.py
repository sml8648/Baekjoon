import sys
input = sys.stdin.readline

a,b,c,d,e = map(int,input().split())
a1,b1,c1,d1,e1 = map(int,input().split())

result1 = 6*a + b*3 + c*2 + d + e*2
result2 = 6*a1 + b1*3 + c1*2 + d1 + e1*2

print(result1, result2)