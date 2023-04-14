import heapq

def dijikstra(start,graph, distance):

    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        cost, now = heapq.heappop(q)

        if distance[now] < cost:
            continue

        for each in graph[now]:
            next = each[0]
            new_cost = cost + each[1]
            if new_cost <= distance[next]:
                distance[next] = new_cost
                heapq.heappush(q, (new_cost, next))

def solution(n,s,a,b,fares):

    graph = [[] for _ in range(n+1)]

    for each in fares:
        graph[each[0]].append((each[1], each[2]))
        graph[each[1]].append((each[0], each[2]))

    distance = [float('inf') for _ in range(n + 1)]

    result = []
    for i in range(n+1):
        if not i:
            distance = [float('inf') for _ in range(n + 1)]
            dijikstra(s,graph, distance)
            first = distance[a]
            second = distance[b]
            result.append(first+second)


        else:
            distance = [float('inf') for _ in range(n + 1)]
            dijikstra(s,graph,distance)
            mid = distance[i]
            distance = [float('inf') for _ in range(n + 1)]
            dijikstra(i,graph,distance)
            first = distance[a]
            second = distance[b]
            result.append(mid+first+second)

    return min(result)