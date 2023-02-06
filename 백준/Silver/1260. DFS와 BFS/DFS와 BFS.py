n,m,v = map(int,input().split())


visited1 = [0]*(n+1)
visited2 = [0]*(n+1)
# 이게 되넹?
line = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    line[a].append(b)
    line[b].append(a)

def dfs(spot):

    print(spot, end=" ")
    visited1[spot] = 1

    for i in sorted(line[spot]):
        if visited1[i] == 0:
            dfs(i)

dfs(v)
print()
def bsf(spot):

    q_list = []
    q_list.append(spot)
    visited2[spot] = 1
    while len(q_list) > 0:
        index = q_list.pop(0)
        print(index,end=" ")
        for i in sorted(line[index]):
            if visited2[i] == 0:
                visited2[i] = 1
                q_list.append(i)

bsf(v)