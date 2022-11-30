

a = int(input())
a_list = list(map(int,input().split()))

count = 0

for each in a_list:
    if each == a:
        count += 1

print(count)