n = input()
arr = list(map(int,input().split()))
D = [1] * len(arr)

for i in range(1,len(arr)):
    for j in range(0,i):
        if arr[i] < arr[j]:
            D[i] = max(D[j] + 1, D[i])

print(max(D))