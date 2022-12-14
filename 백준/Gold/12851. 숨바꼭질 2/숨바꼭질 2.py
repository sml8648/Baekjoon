import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())

if n > k:
    print(n - k)
    print(1)

else:

    visited = [0]*100001

    q = deque()

    q.append((n,[n]))
    
    count = 0
    Shortest_time = 1e9

    while q:
        a, SP = q.popleft()

        if not (len(SP) -1 <= Shortest_time):
            continue

        if a == k:
            if len(SP) - 1 <= Shortest_time:
                Shortest_time = len(SP) - 1
                count += 1

        visited[a] = 1

        for each in [2,1,-1]:
            tmp = a
            if each == 2:
                if 0 <= tmp*each <= 100000:
                    if not visited[tmp*each]:
                        q.append((tmp*each,SP + [tmp*each]))

            else:
                if 0 <= tmp + each <= 100000:
                    if not visited[tmp + each]:
                        q.append((tmp + each,SP +[tmp + each]))

    print(Shortest_time)
    print(count)