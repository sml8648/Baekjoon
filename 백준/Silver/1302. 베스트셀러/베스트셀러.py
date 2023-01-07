from collections import defaultdict
book_name = defaultdict(int)
n = int(input())

for _ in range(n):
    name = str(input())
    book_name[name] += 1

max_value = max(book_name.values())
answer = []
for each in book_name.items():

    if each[1] == max_value:
        answer.append(each[0])

print(sorted(answer)[0])