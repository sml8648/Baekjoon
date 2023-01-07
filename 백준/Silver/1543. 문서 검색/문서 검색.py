a_string = str(input())
target_str = str(input())

i = 0
count = 0
while True:

    if a_string[i:i+len(target_str)] == target_str:
        i += len(target_str)
        count += 1
    else:
        i += 1
    if i > len(a_string):
        break

print(count)