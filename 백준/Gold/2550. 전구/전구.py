import sys
input = sys.stdin.readline

n = int(input())

numbers_1 = list(map(int, input().split()))
numbers_2 = list(map(int,input().split()))

a_dict = {}
b_dict = {}
for idx, each in enumerate(numbers_2):
    a_dict[each] = idx
    b_dict[idx] = each

numbers = []
for each in numbers_1:
    numbers.append(a_dict[each])

answer = [-1]
answer_arr = [1]*len(numbers)
count = 0

for idx, number in enumerate(numbers):
    if answer[-1] < number:
        answer.append(number)
        count += 1
        answer_arr[idx] = count
    else:
        left = 0
        right = len(answer)

        while left < right:
            mid = (right+left)//2
            if answer[mid] < number:
                left = mid+1
            else:
                right = mid
        answer[right] = number
        answer_arr[idx] = right

print(len(answer)-1)
last_result = []

max_value = len(answer) - 1
for i in range(len(answer_arr)-1,-1,-1):

    if answer_arr[i] == max_value:
        max_value -= 1
        last_result.append(numbers_1[i])

last_result.sort()
print(*last_result)