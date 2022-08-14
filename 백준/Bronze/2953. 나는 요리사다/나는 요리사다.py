result_list = []
for _ in range(5):
    result_list.append(sum(list(map(int,input().split()))))

max_value = max(result_list)
print(result_list.index(max_value) + 1, max_value)