import sys
input = sys.stdin.readline

a = int(input())

if a % 4:

    for _ in range((a//4) + 1):
        print('long',end=' ')
    print('int')

else:
    for _ in range((a//4)):
        print('long',end=' ')
    print('int')