import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

visited = [0]*(n+1)

count = 0
q = deque()

q.append((n,count,[n]))

answer = []
ans = -1
while q:

    a,count,SP= q.popleft()
    visited[a] = 1

    if a == 1:
        ans = count
        answer = SP
        break

    for i in [3,2,1]:
        tmp_a = a
        if i != 1 and a % i == 0:
            tmp_a = tmp_a // i
            if not visited[tmp_a]:
                q.append((tmp_a,count+1,SP+[tmp_a]))

        if i == 1:
            if not visited[tmp_a -1]:
                q.append((tmp_a-1,count+1,SP+[tmp_a-1]))

print(ans)
print(*answer)