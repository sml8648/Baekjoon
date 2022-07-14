import sys
input = sys.stdin.readline

a_list = [1]*1000001

for i in range(2, int(1000001**0.5) + 1):
    if a_list[i]:
        for j in range(2*i,1000001, i):
            a_list[j] = 0

while True:
    n = int(input())

    if n == 0:
        break

    for k in range(3, len(a_list)):

        if a_list[k] == 1 and a_list[n-k] == 1:

            print(n, '=', k, '+', n - k)
            break