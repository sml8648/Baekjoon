a_list = set([i+1 for i in range(30)])

for _ in range(28):

    a = int(input())

    if a in a_list:
        a_list.remove(a)

for each in sorted(a_list):
    print(each)
