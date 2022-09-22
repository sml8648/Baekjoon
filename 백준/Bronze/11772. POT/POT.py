n = int(input())

sum = 0
for _ in range(n):

    a = str(input().strip())

    sum += int(a[:-1])**int(a[-1])

print(sum)