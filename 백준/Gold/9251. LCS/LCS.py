one = input()
two = input()

matrix = [[0]*(len(two)+1) for _ in range(len(one) + 1)]


for i in range(1,len(one)+1):
    for j in range(1,len(two)+1):
        if one[i-1] == two[j-1]:
            matrix[i][j] = matrix[i-1][j - 1] + 1
        else:
            matrix[i][j] = max(matrix[i][j - 1], matrix[i - 1][j])
            
print(matrix[-1][-1])
