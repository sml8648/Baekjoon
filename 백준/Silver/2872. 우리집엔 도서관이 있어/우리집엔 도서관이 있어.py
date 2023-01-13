import sys
input = sys.stdin.readline

n = int(input())
books = []

for i in range(1, n+1):
    books.append(int(input()))

max_value = 0
max_index = -1
for i in range(n):
    if max_value < books[i]:
        max_value = books[i]
        max_index = i

length = 1
target = max_value -1
for i in range(max_index -1, -1, -1):
    if target == books[i]:
        target -= 1
        length += 1

print(n - length)
