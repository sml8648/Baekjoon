import sys

input = sys.stdin.readline

a,b = map(int,input().split())
score = list(map(int,input().split()))
score.sort()

print(score[-b])