import sys
input = sys.stdin.readline

n, c = map(int, input().split())

spot = []
for _ in range(n):
    spot.append(int(input()))

spot.sort()

start = 0
end = spot[-1] - spot[0]

answer = -1
while start <= end:

    mid = (end + start) // 2

    first_point = spot[0]
    count = 1
    for i in spot[1:]:
        if i - first_point >= mid:
            count += 1
            first_point = i

    if count >= c:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)