n = int(input())
a_list = list(map(int,input().split()))

result = []
for idx, a in enumerate(a_list):
    position = len(result) - a
    result.insert(position,str(idx+1))

print(' '.join(result))