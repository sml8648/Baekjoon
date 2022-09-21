import sys
input = sys.stdin.readline

n, l, k = map(int,input().split())

count = 0
result = []
for _ in range(n):
    a,b,c = map(int,input().split())

    if a >= k and b >= k and c >= k:
        if (a+b+c) >= l:
            count += 1
            result.append(str(a))
            result.append(str(b))
            result.append(str(c))

print(count)
print(' '.join(result))