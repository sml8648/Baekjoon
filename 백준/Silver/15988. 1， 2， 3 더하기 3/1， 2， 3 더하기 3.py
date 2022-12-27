n = int(input())

dp = [0] * (1000000 + 1)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 1000000 + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009

for _ in range(n):

    a = int(input())
    print(dp[a])
