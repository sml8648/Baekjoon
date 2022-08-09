def solution(n):
    answer = []

    flag = -1
    for i in range(0,18):
        if n < 3**i:
            flag = i-1
            break

    m = n
    while flag != -1:
        tmp = 3**flag
        a = m // tmp
        answer.append(a)
        m = m % tmp

        flag -= 1

    result = 0
    for idx, each in enumerate(answer):
        result += each*(3**idx)

    return result