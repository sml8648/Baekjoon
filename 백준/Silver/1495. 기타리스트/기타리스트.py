import sys
input = sys.stdin.readline
n, s, m = map(int,input().split())
volume = list(map(int,input().split()))

dp = [[0]*(m+1) for _ in range(n+1)]

dp[0][s] = 1

for idx, each in enumerate(volume):

    for idx2, k in enumerate(dp[idx]):

        if k:

            upper = idx2 + each
            lower = idx2 - each

            if upper <= m:
                dp[idx+1][upper] = 1

            if lower >= 0:
                dp[idx+1][lower] = 1

max_value = -1
for idx, each in enumerate(dp[n]):
    if each:
        if idx > max_value:
            max_value = idx

print(max_value)