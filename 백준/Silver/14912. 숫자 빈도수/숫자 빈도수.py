a, b = map(int,input().split())

count = 0
for i in range(1,a+1):

    tmp = str(i)
    for j in tmp:
        if j == str(b):
            count +=1

print(count)
