n = int(input())

def tropy_count(arr):

    min_value = -1
    count = 0
    for each in arr:
        if each > min_value:
            min_value = each
            count += 1

    return count

def tropy_count2(arr):

    min_value = arr[0]
    count = 0
    for each in arr:
        if each > min_value:
            min_value = each
            count += 1

    return count

arr = []
for _ in range(n):
    a = int(input())
    arr.append(a)

print(tropy_count(arr))
print(tropy_count(arr[::-1]))