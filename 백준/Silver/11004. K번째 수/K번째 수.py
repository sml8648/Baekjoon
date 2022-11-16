import sys
input = sys.stdin.readline
a,b = map(int,input().split())
a_list = list(map(int,input().split()))
a_list.sort()
print(a_list[b-1])