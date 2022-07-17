a,b = map(int,input().split())

a_matrix = []
b_matrix = []
for i in range(2):

    for _ in range(a):
        tmp_arr = list(map(int,input().split()))

        if not i:
            a_matrix.append(tmp_arr)
        else:
            b_matrix.append(tmp_arr)

result_matrix = []
for i in range(a):
    tmp_arr = []
    for j in range(b):
        tmp = a_matrix[i][j] + b_matrix[i][j]
        tmp_arr.append(tmp)
    result_matrix.append(tmp_arr)

for each in result_matrix:

    for k in each:
        print(k,end=' ')
    print()