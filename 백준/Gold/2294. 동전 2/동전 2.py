n, k = map(int,input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [0] + [1e9]*k

for each in coins:

    for i in range(each, k+1):
        dp[i] = min(dp[i], dp[i-each] + 1)
    #     div, mod = divmod(idx, each)
    #     if div == 0: continue
    #     dp[idx] = min(div + dp[mod],dp[idx])
    #
    # print(dp)

if dp[k] == 1e9:
    print(-1)
else:
    print(dp[k])
