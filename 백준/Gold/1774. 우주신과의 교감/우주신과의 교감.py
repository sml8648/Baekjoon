import math
import sys
input = sys.stdin.readline

def find_parent(parent,x):

    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)

edges = []
result = 0

for i in range(1, v+1):
    parent[i] = i

tmp_list = []
for _ in range(v):
    a,b = map(float,input().split())
    tmp_list.append((a,b))

already_list = set()
for _ in range(e):
    a,b = map(int,input().split())
    union_parent(parent,a,b)

for idx1, each in enumerate(tmp_list):
    for idx2, k in enumerate(tmp_list):
        if idx1 == idx2:
            continue

        tmp_cost = (each[0] - k[0])**2 + (each[1] - k[1])**2
        tmp_cost = math.sqrt(tmp_cost)
        edges.append((tmp_cost,idx1+1,idx2+1))

edges.sort()

for edge in edges:
    cost, a, b = edge

    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(f"{result:.2f}")