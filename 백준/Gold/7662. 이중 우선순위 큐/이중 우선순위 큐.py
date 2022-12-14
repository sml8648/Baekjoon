import heapq
import sys
input = sys.stdin.readline

K = int(input())

for _ in range(K):

    n = int(input())
    q_1 = []
    q_2 = []
    visited = [False]*n
    for i in range(n):

        a,b = input().split()

        if a == 'I':
            heapq.heappush(q_1,(int(b),i))
            heapq.heappush(q_2,(-int(b),i))
            visited[i] = True

        else:
            if b == '-1':
                while q_1 and (visited[q_1[0][1]] == False):
                    heapq.heappop(q_1)
                if q_1:
                    visited[q_1[0][1]] = False
                    heapq.heappop(q_1)
            else:
                while q_2 and (visited[q_2[0][1]] == False):
                    heapq.heappop(q_2)
                if q_2:
                    visited[q_2[0][1]] = False
                    heapq.heappop(q_2)

    while q_1 and (visited[q_1[0][1]] == False):
        heapq.heappop(q_1)
    while q_2 and (visited[q_2[0][1]] == False):
        heapq.heappop(q_2)

    if not q_1 or not q_2:
        print('EMPTY')
    else:
        print(-q_2[0][0], q_1[0][0])