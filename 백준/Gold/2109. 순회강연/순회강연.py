import sys
input = sys.stdin.readline
import heapq
n = int(input())

homework_list = []
for each in range(n):
    a, b = map(int,input().split())


    homework_list.append((b,a))

homework_list.sort(key=lambda x:x[0])

q = []
today = 1
total_score = 0
for each in homework_list:

    due, score = each

    if len(q) < due:
        heapq.heappush(q,(score, due))
        total_score += score
    else:

        score2, due2 = heapq.heappop(q)

        if score > score2:
            heapq.heappush(q, (score, due))
            total_score -= score2
            total_score += score
        else:
            heapq.heappush(q, (score2, due2))

print(total_score)