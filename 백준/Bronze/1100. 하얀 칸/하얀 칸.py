import sys
input = sys.stdin.readline

count = 0

for i in range(8):
    tmp = str(input().strip())

    for idx, j in enumerate(tmp):
        if (i % 2 == 0) and (idx % 2 == 0) and j == 'F':
            count += 1
        elif (i % 2 == 1) and (idx % 2 == 1) and j == 'F':
            count += 1

print(count)
