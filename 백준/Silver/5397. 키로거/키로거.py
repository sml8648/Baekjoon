import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):

    tmp_str = str(input().strip())

    left_stack = []
    right_stack = []

    for each in tmp_str:

        if each == '<':
            if len(left_stack):
                tmp = left_stack.pop()
                right_stack.append(tmp)
        elif each == '>':

            if len(right_stack):
                tmp = right_stack.pop()
                left_stack.append(tmp)

        elif each == '-':
            if len(left_stack):
                tmp = left_stack.pop()
        else:
            left_stack.append(each)

    print(''.join(left_stack), end='')
    print(''.join(right_stack[::-1]))