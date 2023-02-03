import sys
input = sys.stdin.readline
import heapq

n = int(input())

q = []
for _ in range(n):

    tmp_list = list(map(int,input().split()))

    for each in tmp_list:
        heapq.heappush(q,each)

        if len(q) > n:
            heapq.heappop(q)

print(heapq.heappop(q))