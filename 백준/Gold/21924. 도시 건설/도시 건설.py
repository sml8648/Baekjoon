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

cost_sum = 0
for _ in range(e):
    a, b, cost = map(int,input().split())
    cost_sum += cost
    edges.append((cost,a,b))

edges.sort()

for edge in edges:
    cost, a, b = edge

    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

for edge in edges:
    cost, a, b = edge
    union_parent(parent,a,b)
# print(cost - result)

final = set(parent[1:])
if len(final) == 1:
    print(cost_sum - result)
else:
    print(-1)