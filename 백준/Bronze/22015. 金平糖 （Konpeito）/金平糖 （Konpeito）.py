tmp = list(map(int,input().split()))

result = 0

for each in tmp:
    result += (max(tmp) - each)
    
print(result)