import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = input().strip()

deleted = 0
stack = []
for x in data:

    while len(stack) > 0 and stack[-1] < x:

        if deleted == k:
            break
        else:
            stack.pop()
            deleted += 1
    stack.append(x)

for i in range(k - deleted):
    stack.pop()

print(''.join(stack))