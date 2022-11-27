n = int(input())

for _ in range(n):
    a, b = map(int, input().split())

    result = divmod(a, b)

    if result[1]:
        print(result[0] + 1)
    else:
        print(result[0])