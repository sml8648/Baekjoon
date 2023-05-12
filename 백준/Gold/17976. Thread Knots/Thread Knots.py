import sys
input = sys.stdin.readline
n = int(input())

lines = []
for _ in range(n):
    a,b = map(int,input().split())
    lines.append((a,b))

lines.sort()

def search(x):

    before = lines[0][0]

    for each in lines[1:]:

        now = each[0]
        if now - before < x:
            tmp = before + x

            if each[0] <= tmp <= each[0] + each[1]:
                before = tmp
            else:
                return False
        else:
            before = now

    return True

start = -1
end = 2000000001

while start <= end:

    mid = (start + end) // 2
    result = search(mid)

    # 이분탐색으로 문제 풀이
    if result:
        start = mid + 1
    else:
        end = mid - 1

if result: print(mid)
else: print(mid-1)