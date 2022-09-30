import sys
input = sys.stdin.readline

while True:

    a = str(input().strip())
    if a == '#':
        break

    a = a.split()
    result = []
    for each in a:
        result.append(each[::-1])

    print(' '.join(result))