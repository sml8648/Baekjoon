import sys
input = sys.stdin.readline

while True:

    a = str(input())
    if a[:-1] == '***':
        break
    else:
        result = a[:-1]
        print(result[::-1])