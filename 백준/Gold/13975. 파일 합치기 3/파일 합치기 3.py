import sys
input = sys.stdin.readline
import heapq

n = int(input())

for _ in range(n):

    k = int(input())
    q = []
    number_list = list(map(int,input().split()))

    cost = 0
    for each in number_list:
        heapq.heappush(q,each)

    while q:
        if len(q) > 1:
            first = heapq.heappop(q)
            second = heapq.heappop(q)

            cost += (first + second)

            heapq.heappush(q,first+second)
        elif len(q) == 1:
            result = heapq.heappop(q)
            print(cost)
