def solution(n,m,section):

    pointer = 0
    checked = [False]*(n+1)

    for i in range(section[0]):
        checked[i] = True

    count = 0
    for each in section:

        if checked[each]:
            continue

        count += 1
        pointer = each
        for k in range(each, each+m):

            if k > n: continue
            checked[k] = True

    return count