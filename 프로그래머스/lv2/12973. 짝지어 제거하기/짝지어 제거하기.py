def solution(s):

    stack = []
    for each in s:
        stack.append(each)

    sub_stack = ['0']
    for _ in range(len(s)):

        current = stack.pop()

        if sub_stack[-1] == current:
            sub_stack.pop()
        else:
            sub_stack.append(current)

    if len(sub_stack) == 1:
        return 1
    else:
        return 0