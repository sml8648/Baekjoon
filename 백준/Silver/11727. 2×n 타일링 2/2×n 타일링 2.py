import sys
input = sys.stdin.readline

n = [0]*1001

n[1] = 1
n[2] = 3

for i in range(3,len(n)):

    n[i] = n[i-1] + n[i-2]*2

print(n[int(input())]%10007)