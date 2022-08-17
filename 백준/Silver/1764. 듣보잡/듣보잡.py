import sys
n, m = map(int,sys.stdin.readline().split())

one = []
for _ in range(n):
    name = sys.stdin.readline().strip()
    one.append(name)

two = []
for _ in range(m):
    name = input()
    two.append(name)

one = set(one)
two = set(two)

result = one.intersection(two)

print(len(result))
for each in sorted(list(result)):
    print(each)