import sys
input = sys.stdin.readline

m, n = map(int, input().split())

def find_parent(x):

    # if x == parent[x]:
    #     return x
    # else:
    #     return find_parent(parent[x])

    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x,y):

    x = find_parent(x)
    y = find_parent(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    # X = find_parent(x)
    # Y = find_parent(y)
    #
    # if X < Y:
    #     parent[y] = X
    # elif Y < X:
    #     parent[x] = Y

parent = [i for i in range(m)]

count = 0

cycle = False
for i in range(n):
    a, b = map(int,input().split())

    if find_parent(a) == find_parent(b):
        cycle = True
        print(i + 1)
        break
    else:
        union_parent(a,b)

if not cycle:
    print(0)