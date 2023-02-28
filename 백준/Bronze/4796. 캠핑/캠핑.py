import sys
input = sys.stdin.readline

count = 1
while True:

    L, P, V = map(int,input().split())

    if not L and not P and not V:
        break

    tmp = V // P
    left = V % P

    result = tmp * L

    if left > L:
        result += L
    else:
        result += left

    print(f"Case {count}:",result)
    count += 1