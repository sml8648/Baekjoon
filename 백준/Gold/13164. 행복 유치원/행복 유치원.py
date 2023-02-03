import sys
input = sys.stdin.readline

n, k = map(int,input().split())

child_list = list(map(int,input().split()))

diff = []
for child1, child2 in zip(child_list, child_list[1:]):
    diff.append(child2 - child1)

diff.sort()

for each in range(k-1):
    diff.pop()

print(sum(diff))