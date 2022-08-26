n = int(input())

sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
axis = 0
for _ in range(n):
    a,b = map(int,input().split())

    if a > 0 and b > 0:
        sum1 += 1
    elif a > 0 and b < 0:
        sum4 += 1
    elif a < 0 and b < 0:
        sum3 += 1
    elif a <0 and b > 0:
        sum2 += 1
    elif a == 0 or b == 0:
        axis += 1

print("Q1:",sum1)
print("Q2:",sum2)
print("Q3:",sum3)
print("Q4:",sum4)
print("AXIS:",axis)