import sys
input = sys.stdin.readline

m = int(input())

for _ in range(m):

    n = int(input())
    numbers = []
    for _ in range(n):
        numbers.append(int(input()))

    answer = [-1]
    for idx, number in enumerate(numbers):
        if answer[-1] < number:
            answer.append(number)
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

    print(len(answer)-1)