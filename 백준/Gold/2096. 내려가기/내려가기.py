import sys
input = sys.stdin.readline

N = int(input())

matrix = list(map(int,input().split()))

max_matrix = matrix
min_matrix = matrix

for _ in range(N-1):
    a, b, c = map(int,input().split())

    new_a = max(a + max_matrix[0], a + max_matrix[1])
    new_b = max(b + max_matrix[0], b + max_matrix[1], b + max_matrix[2])
    new_c = max(c + max_matrix[1], c + max_matrix[2])

    max_matrix = [new_a,new_b,new_c]

    new_a = min(a + min_matrix[0], a + min_matrix[1])
    new_b = min(b + min_matrix[0], b + min_matrix[1], b + min_matrix[2])
    new_c = min(c + min_matrix[1], c + min_matrix[2])

    min_matrix = [new_a,new_b,new_c]

print(max(max_matrix))
print(min(min_matrix))