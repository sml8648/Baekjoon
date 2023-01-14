import sys
input = sys.stdin.readline

import heapq

n = int(input())
tmp_list = []
for _ in range(n):
    a, b = map(int,input().split())
    tmp_list.append((a,b))
tmp_list.sort()

room = []
heapq.heappush(room, tmp_list[0][1])

for i in range(1, n):

    if room[0] > tmp_list[i][0]:
        heapq.heappush(room, tmp_list[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, tmp_list[i][1])

print(len(room))