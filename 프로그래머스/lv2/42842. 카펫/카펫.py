def solution(brown, yellow):

    total = brown + yellow

    a_list = []
    tmp = int(total ** (1/2))

    for i in range(3,tmp+1):

        if total % i == 0:
            a_list.append([i,total // i])

    for idx, i in enumerate(a_list):

        x,y = i[0], i[1]
        tmp = (x+y-2)*2

        if brown >= tmp:
            a_list[idx].sort(reverse=True)
            return a_list[idx]
