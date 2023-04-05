def check_correct(p):
    tmp = [0]
    for each in p:
        if each == '(':
            tmp.append(each)
        elif each == ')':
            if tmp[-1] == '(':
                tmp.pop()

    return True if len(tmp) == 1 else False


def stage_one(p):
    if not len(p): return ''

    left = 0
    right = 0
    for idx, each in enumerate(p):

        if each == '(': left += 1
        if each == ')': right += 1
        if left == right: break

    u = p[:idx + 1]
    v = p[idx + 1:]

    return u, v


def solution(p):
    result = stage_one(p)
    if result == '': return ''

    if check_correct(result[0]):

        u = result[0]
        v = result[1]
        new_v = solution(v)
        tmp_result = u + new_v

    else:
        u = result[0]
        v = result[1]
        new_v = solution(v)

        tmp_result = '(' + new_v + ')'

        for char in u[1:-1]:
            if char == ')': tmp_result += '('
            if char == '(': tmp_result += ')'

    return tmp_result