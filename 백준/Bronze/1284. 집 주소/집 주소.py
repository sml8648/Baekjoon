import sys
input = sys.stdin.readline

while True:

    a = str(input().strip())
    if int(a) == 0:
        break

    answer = 0
    for i in a:

        if int(i) == 1:
            answer += 2
        elif int(i) == 0:
            answer += 4
        else:
            answer += 3

    print(answer + len(a) + 1)