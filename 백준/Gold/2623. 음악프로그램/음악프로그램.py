from collections import deque

v,e = map(int,input().split())

indegree = [0] * (v+1)

graph = [[] for i in range(v+1)]

for _ in range(e):
    singers = list(map(int,input().split()))

    for a, b in zip(singers[1:],singers[2:]):

        graph[a].append(b)
        indegree[b] += 1


result = []

def topology_sort():
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:

        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

topology_sort()

if len(result) != v:
    print(0)
else:
    for each in result:
        print(each,end=' ')