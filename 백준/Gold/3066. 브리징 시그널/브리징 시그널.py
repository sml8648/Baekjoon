import sys
input = sys.stdin.readline

m = int(input())

for _ in range(m):

    n = int(input())
    numbers = []
    for _ in range(n):
        numbers.append(int(input()))

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