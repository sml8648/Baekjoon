import sys
input = sys.stdin.readline

for test_case in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    
    max_dif = 0
    for i in range(n - 2):
        dif = abs(arr[i] - arr[i+2])
        max_dif = max(max_dif, dif)
    print(max_dif)