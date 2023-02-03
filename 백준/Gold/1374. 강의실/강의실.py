import sys
input = sys.stdin.readline
import heapq

n = int(input())

a_list = []
for _ in range(n):
    a, b, c = map(int,input().split())

    a_list.append((c,b))

a_list.sort(key=lambda x : x[1])

q = []
heapq.heappush(q,a_list[0])
count = 1

for each in a_list[1:]:

    end_time, start_time = heapq.heappop(q)

    if each[1] < end_time:
        heapq.heappush(q, (end_time, start_time))
        heapq.heappush(q, (each[0], each[1]))
        count += 1
    else:
        heapq.heappush(q, (each[0], each[1]))

print(count)