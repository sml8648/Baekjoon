from collections import defaultdict
a, b, c = map(int, input().split())

int_dict = defaultdict(int)

for i in range(1,a+1):
    for j in range(1,b+1):
        for k in range(1,c+1):

            tmp = i + j + k
            int_dict[tmp] += 1

result = dict(sorted(int_dict.items(), key=lambda item: item[1], reverse=True))

print(list(result.items())[0][0])