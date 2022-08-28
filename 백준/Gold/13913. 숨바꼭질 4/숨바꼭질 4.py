import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())

if n > k:
    print(n-k)
    for i in range(n,k-1,-1):
        print(i,end=' ')
else:
    visited = [0]*100001

    q = deque()

    q.append((n,[n]))

    Shortest_path = []
    while q:
        a, SP = q.popleft()

        if a == k:
            Shortest_path = SP
            break

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

    print(len(Shortest_path) - 1)
    print(*Shortest_path)