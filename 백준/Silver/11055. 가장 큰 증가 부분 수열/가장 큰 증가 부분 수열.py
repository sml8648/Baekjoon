n = input()
arr = list(map(int,input().split()))

D = [0] * len(arr)

for i in range(0,len(arr)):
    D[i] = arr[i]
    for j in range(0,i):
        if arr[i] > arr[j]:
            D[i] = max(D[i],D[j] + arr[i])
print(max(D))