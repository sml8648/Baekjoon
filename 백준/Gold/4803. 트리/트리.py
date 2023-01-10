import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

def is_cycle(x, prev):
    visited[x] = True
    for y in graph[x]:
        if visited[y]:
            if y!= prev:
                return True
        else:
            if is_cycle(y, x):
                return True
    return False

test_case = 1
while True:
    n, m = map(int,input().split())
    if n == 0 and m == 0:
        break

    graph =[[] for _ in range(n + 1)]
    visited = [False]*(n+1)

    for i in range(m):
        x, y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)

    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            if not is_cycle(i, 0):
                cnt += 1

    if cnt == 0:
        print(f'Case {test_case}: No trees.')
    elif cnt == 1:
        print(f'Case {test_case}: There is one tree.')
    else:
        print(f'Case {test_case}: A forest of {cnt} trees.')

    test_case += 1