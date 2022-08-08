one = input()
two = input()

matrix = [[0] * (len(two) + 1) for _ in range(len(one) + 1)]

for i in range(1, len(one) + 1):
    for j in range(1, len(two) + 1):
        if one[i - 1] == two[j - 1]:
            matrix[i][j] = matrix[i - 1][j - 1] + 1

        else:
            matrix[i][j] = max(matrix[i][j - 1], matrix[i - 1][j])

print(matrix[-1][-1])
result_list = []

i = len(one)
j = len(two)

while len(result_list) != matrix[-1][-1]:

    if matrix[i][j] == matrix[i][j-1]:
        j -= 1
    elif matrix[i][j] == matrix[i-1][j]:
        i -= 1
    else:
        result_list.append(two[j-1])
        i -= 1

for each in result_list[::-1]:
    print(each,end='')