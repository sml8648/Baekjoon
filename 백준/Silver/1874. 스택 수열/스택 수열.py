import sys
input = sys.stdin.readline

n = int(input())

count = 1
s = []
temp = True
answer = []
for _ in range(n):

    a = int(input())

    while count <= a:
        s.append(count)
        answer.append('+')
        count += 1

    if s[-1] == a:
        s.pop()
        answer.append('-')

    else:
        temp = False

if temp == False:
    print('NO')
else:
    for each in answer:
        print(each)