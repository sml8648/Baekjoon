import sys
input = sys.stdin.readline

for test_case in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    max_value = arr[n - 1]
    target = [0] * n
    for i in range(n - 1, -1, -1):
        max_value = max(max_value, arr[i])
        target[i] = max_value
    result = 0
    for i in range(n):
        result += max(0, target[i] - arr[i])
    print(result)