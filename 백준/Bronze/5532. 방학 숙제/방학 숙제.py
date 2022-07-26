L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

if A % C:
    tmp_a = (A // C) + 1
else:
    tmp_a = (A // C)

if B % D:
    tmp_b = (B // D) + 1
else:
    tmp_b = (B // D)

print(L - max(tmp_a,tmp_b))