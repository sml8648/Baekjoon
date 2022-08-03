base_str = '9780921418'
base_str += str(input().strip())
base_str += str(input().strip())
base_str += str(input().strip())

sum = 0

for idx, each in enumerate(base_str):

    if idx % 2:

        sum += 3*int(each)
    else:
        sum += 1*int(each)

print('The 1-3-sum is',sum)