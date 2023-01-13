import sys
input = sys.stdin.readline
import heapq

n, k = map(int,input().split())

stones = []
for i in range(n):
    weight, price = map(int,input().split())
    stones.append((weight, price))

bags = []
for i in range(k):
    bag = int(input())
    bags.append(bag)

stones.sort()
bags.sort()

heap = []
cur = 0
result = 0
for bag in bags:
    while cur < n:
        weight, price = stones[cur]
        if bag >= weight:
            heapq.heappush(heap, -price)
            cur += 1
        else:
            break
    if len(heap) > 0:
        price = -heapq.heappop(heap)
        result += price

print(result)