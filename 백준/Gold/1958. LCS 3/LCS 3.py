one = str(input().strip())
two = str(input().strip())
three = str(input().strip())

matrix = [[[0] * (len(one) + 1) for _ in range(len(two) + 1)] for _ in range(len(three) + 1)]



for i in range(1, len(three) + 1):
    for j in range(1, len(two) + 1):
        for k in range(1, len(one) + 1):
            if three[i - 1] == two[j - 1] and two[j-1] == one[k-1]:
                matrix[i][j][k] = matrix[i - 1][j - 1][k-1] + 1

            else:
                matrix[i][j][k] = max(matrix[i][j - 1][k], matrix[i - 1][j][k], matrix[i][j][k-1])

print(matrix[-1][-1][-1])