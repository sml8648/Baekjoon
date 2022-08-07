import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
answer = [0]

for number in numbers:
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

print(n - (len(answer)-1))