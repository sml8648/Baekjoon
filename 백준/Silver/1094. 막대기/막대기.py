a = bin(int(input()))

count = 0
for each in str(a[2:]):
    if each == '1':
        count += 1
print(count)