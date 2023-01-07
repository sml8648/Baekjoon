n, m = map(int,input().split())

arr = []
for _ in range(n):
    weight, value = map(int,input().split())
    arr.append([weight,value])

matrix = [[0]*(m+1) for _ in range(n)]

def Value_Calc(n,m):
    if n == -1:
        return 0
    if matrix[n][m] != 0:
        return matrix[n][m]
    weight = arr[n][0]
    value = arr[n][1]

    if m - weight < 0:
        matrix[n][m] = Value_Calc(n-1,m)
        return matrix[n][m]
    else:
        matrix[n][m] = max(Value_Calc(n-1,m-weight) + value,Value_Calc(n-1,m))
        return matrix[n][m]

print(Value_Calc(n-1,m))