import sys
input = sys.stdin.readline

n = int(input())
stack = []
answer = []
current = 1

for _ in range(n):
    x = int(input())
    while len(stack) == 0 or stack[-1] < x:
        stack.append(current)
        current += 1
        answer.append('+')

    if stack[-1] == x:
        stack.pop()
        answer.append('-')
    else:
        answer = ['NO']
        break

for x in answer:
    print(x)