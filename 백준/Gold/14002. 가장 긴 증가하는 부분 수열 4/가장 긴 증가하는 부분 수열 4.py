n = input()
arr = list(map(int,input().split()))
D = [1] * len(arr)

for i in range(1,len(arr)):
    for j in range(0,i):
        if arr[i] > arr[j]:
            D[i] = max(D[j] + 1, D[i])

print(max(D))

tmp = max(D)
a_list = []
for i in range(len(D),0,-1):

  if D[i-1] == tmp:
    a_list.append(arr[i-1])
    tmp -= 1

a_list.sort()
print(*a_list)