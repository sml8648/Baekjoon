from collections import Counter

a = int(input())

a_list = []

for _ in range(a):

    a_list.append(list(map(int,input().split())))

result = list(zip(*a_list))

score = [0]*a

for each in result:
    tmp = Counter(each)

    for idx,k in enumerate(each):

        if tmp[k] > 1:
            continue
        else:
            score[idx] += k

for each in score:
    print(each)