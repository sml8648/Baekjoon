count = 0
while True:
    
    tmp_list = list(map(int,input().split()))
    if tmp_list[0] == 0:
        break
    else:
        count += 1
        print(f'Case {count}: Sorting... done!')