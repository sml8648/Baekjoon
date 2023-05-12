import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

n = int(input())
cost = [0] + list(map(int,input().split()))

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0, cost[i]] for i in range(n+1)]
visited = [0]*(n+1)

def count_tree(x):

    visited[x] = 1

    for child in graph[x]:
        if not visited[child]:
            count_tree(child)
            dp[x][1] += dp[child][0]
            dp[x][0] += max(dp[child][0], dp[child][1])

count_tree(1)

print(max(dp[1][1], dp[1][0]))