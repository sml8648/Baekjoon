import sys
input = sys.stdin.readline

n = int(input())

poll = {}
reverse_poll = {}
void_arr = set()
for i in range(n):
    void_arr.add(i)
    k, v = map(int,input().split())
    poll[k] = v
    reverse_poll[v] = k

b = sorted(poll.keys())

numbers = []
for i in b:
    numbers.append(poll[i])

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

print(n - (len(answer)-1))

last_result = []
max_value = len(answer) - 1
for i in range(len(answer_arr)-1,-1,-1):

    if answer_arr[i] == max_value:
        max_value -= 1
        void_arr.discard(i)
        #last_result.append(numbers_1[i])

final_result = []
for each in list(void_arr):
    final_result.append(reverse_poll[numbers[each]])

final_result.sort()
for each in final_result:
    print(each)
