import sys
input = sys.stdin.readline

string = str(input().strip())
bomb = str(input().strip())

lastChar = bomb[-1]
stack = []
length = len(bomb)

for char in string:
    stack.append(char)
    if char == lastChar and ''.join(stack[-length:]) == bomb:
        del stack[-length:]

answer = ''.join(stack)

if answer == '':
    print("FRULA")
else:
    print(answer)