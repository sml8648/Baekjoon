import sys
n = str(input().rstrip())
n = sorted(n, reverse=True)

if '0' not in n:
    print(-1)
else:
    sum = 0
    for k in n:
        sum += int(k)

    if sum % 3 == 0:
        print(''.join(n))
    else:
        print(-1)