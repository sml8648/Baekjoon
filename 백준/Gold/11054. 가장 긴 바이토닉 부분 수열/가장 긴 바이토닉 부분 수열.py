import sys
n = int(sys.stdin.readline())
input_list = list(map(int,sys.stdin.readline().split()))

reverse_list = input_list[::-1]
DI = [1] * n
DR = [1] * n
for i in range(1, n):
    for j in range(i):
        if input_list[i] > input_list[j]:
            DI[i] = max(DI[i], DI[j] + 1)
        if reverse_list[i] > reverse_list[j]:
            DR[i] = max(DR[i], DR[j] + 1)

DR.reverse()

result_list = []
for i in range(n):
    result_list.append(DI[i] + DR[i] - 1)

print(max(result_list))