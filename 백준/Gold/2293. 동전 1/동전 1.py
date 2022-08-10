n,k = map(int,input().split())
coin = [int(input()) for i in range(n)]

dp = [0 for i in range(k+1)]
dp[0] = 1

for each in coin:
    for j in range(each, k+1):
        if j - each >= 0:
            dp[j] += dp[j-each]

print(dp[k])