import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find_parent(parent,x):

    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):

    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n = int(input())
m = int(input())

parent = [0] * (n+1)
for i in range(1,n+1):
    parent[i] = i

for i in range(n):
    tmp_list = list(map(int,input().split()))
    for idx, each in enumerate(tmp_list):
        if each == 1:
            union_parent(parent,i+1,idx+1)

target_list = list(map(int,input().split()))

flag = 0
for one, two in zip(target_list,target_list[1:]):

    if parent[one] != parent[two]:
        flag = 1

if flag:
    print("NO")
else:
    print('YES')