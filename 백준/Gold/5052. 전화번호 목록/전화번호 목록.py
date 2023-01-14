import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    nums = [input().strip() for _ in range(n)]
    nums.sort()

    flag = True
    for i in range(n-1):
        long = len(nums[i])
        if nums[i] == nums[i+1][:long]:
            flag = False
            break
    if flag:
        print('YES')
    else:
        print('NO')