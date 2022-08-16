n,a = map(int,input().split())

divider = set()
for i in range(1,int(n**1/2) + 1):

    if n % i == 0:
        divider.add(n//i)
        divider.add(i)

try:
    divider = list(sorted(divider))
    print(divider[a-1])

except:
    print(0)
