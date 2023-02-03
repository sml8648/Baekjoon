import sys
input = sys.stdin.readline

n, l = map(int,input().split())

leak_point = list(map(int,input().split()))
leak_point.sort()

start_point = -1
end_point = -1

answer = 0
for idx, each in enumerate(leak_point):

    if start_point == -1:
        start_point = each - 0.5
        end_point = each + 0.5
    else:
        end_point = each + 0.5

    length = end_point - start_point

    if length == l:
        answer += 1
        start_point = -1
    elif length > l:
        answer += 1
        start_point = each - 0.5

        if idx + 1 == n:
            answer += 1
    else:
        if idx + 1 == n:
            answer += 1

print(answer)