from collections import deque
def solution(n, path, order):
    
    if n == 2:
        return False
    
    graph = [[] for _ in range(n)]
    indegree = [0] * n
    indegree[0] = 0

    for each in path:
        graph[each[0]].append(each[1])
        graph[each[1]].append(each[0])

    q = deque()
    q.append([0, 0])
    visited = set([0])
    result = []
    while q:
        now, before = q.popleft()
        result.append([before, now])
        for each in graph[now]:
            if each not in visited:
                visited.add(each)
                q.append([each, now])

    graph = [[] for _ in range(n)]
    for each in order: result.append(each)

    for each in result[1:]:
        graph[each[0]].append(each[1])
        indegree[each[1]] += 1

    q = deque()
    q.append(0)

    
    visited = set()
    while q:

        now = q.popleft()
        visited.add(now)
        
        for each in graph[now]:

            indegree[each] -= 1

            if not indegree[each]:
                q.append(each)
    
    if len(visited) == n:
        return True
    else:
        return False