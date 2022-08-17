import math

t = int(input())

for _ in range(t):

    a = int(input())

    result = math.factorial(a)

    while True:

        if result % 10 != 0:
            break
        else:
            result = result // 10

    print(str(result)[-1])