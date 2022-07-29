a_list = list(map(int,input().split()))
x,y,z = map(int,input().split())

flag = 0
for idx,each in enumerate(a_list):

    if each == x:
        flag = idx + 1
        break
        
print(flag)