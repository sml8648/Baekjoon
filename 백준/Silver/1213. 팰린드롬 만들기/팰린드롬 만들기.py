import sys
input = sys.stdin.readline


a_dict = dict()
for k in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':

    a_dict[k] = 0

a_str = str(input().strip())

for each in a_str:
    
    a_dict[each] += 1

answer_list = []
middle = ''
for k,v in a_dict.items():

    if v % 2 == 0:
        tmp = v // 2

        for _ in range(tmp):
            answer_list.append(k)

    else:
        if middle == '':
            middle = k
            tmp = v // 2

            for _ in range(tmp):
                answer_list.append(k)

        else:
            middle = "I'm Sorry Hansoo"
            break

if middle == "I'm Sorry Hansoo":
    print(middle)
else:
    answer_list.sort()
    print(''.join(answer_list),end='')
    print(middle,end='')
    answer_list.sort(reverse=True)
    print(''.join(answer_list))
