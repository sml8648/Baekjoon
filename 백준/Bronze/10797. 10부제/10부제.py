from collections import Counter

a = int(input())

a_list = list(map(int,input().split()))

a_list = Counter(a_list)

print(a_list[a])