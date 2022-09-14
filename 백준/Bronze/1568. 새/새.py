a = int(input())

count = 0
idx = 1
sum = 0

while True:

    sum += idx
    count += 1

    if sum < a :
        idx += 1

    elif sum == a:
        break

    elif sum > a:
        sum -= idx
        count -= 1
        idx = 1

print(count)