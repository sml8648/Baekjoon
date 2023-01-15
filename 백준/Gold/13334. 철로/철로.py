import sys
input = sys.stdin.readline
import heapq

n = int(input())
lines = []

for i in range(n):
    start, end = map(int,input().split())

    if end < start:
        start, end = end, start

    lines.append((start,end))

lines.sort(key=lambda x: x[1])
d = int(input())

heap = []
cur = 0
result = 0
for line in lines:
    start, end = line
    if end - start > d:
        continue
    cur = end
    heapq.heappush(heap, start)
    while len(heap) > 0:
        start = heapq.heappop(heap)

        if cur - start > d:
            continue
        else:
            heapq.heappush(heap, start)
            break

    result = max(result, len(heap))

print(result)