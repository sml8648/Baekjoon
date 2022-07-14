import sys
input = sys.stdin.readline

n,k = map(int,input().split())

a_list = [0]*(n+1)

count = 0
flag = 0
for i in range(2,n+1):

    for j in range(2, n+1):

        if j % i == 0 and a_list[j] == 0:
            count += 1
            a_list[j] = 1

            if count == k:
                flag = j
                break
    if flag:
        break

print(flag)