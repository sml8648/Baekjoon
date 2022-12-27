n = int(input())

for _ in range(n):

    a = int(input())

    tmp_list = []
    for _ in range(a):
        q, p = map(int,input().split())
        tmp_list.append((q,p))

    aaa = sorted(tmp_list)

    best_score = 1000000
    count = 0
    for idx, each in enumerate(aaa):
        if best_score > each[1]:
            count += 1
            best_score = each[1]

    print(count)