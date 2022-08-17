n,m = map(int,input().split())
n_list = set()
for _ in range(n):
    n_list.add(str(input()))

cnt = 0
for _ in range(m):
    t = str(input())
    if t in n_list:
        cnt += 1
print(cnt)
    