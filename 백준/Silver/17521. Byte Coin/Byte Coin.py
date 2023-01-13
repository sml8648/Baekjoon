import sys
input = sys.stdin.readline

n, w = map(int,input().split(' '))

prices = []
for i in range(n):
    prices.append(int(input()))

for i in range(n -1):

    if prices[i] < prices[i + 1]:

        cnt = w // prices[i]
        w += cnt * (prices[i + 1] - prices[i])

print(w)