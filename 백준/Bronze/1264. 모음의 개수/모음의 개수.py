while True:

    a_str = str(input().strip())

    if a_str == '#':
        break

    a_list = ['a', 'e', 'o', 'u', 'i','A','E','O','U','I']

    count = 0
    for each in a_str:
        if each in a_list:
            count += 1

    print(count)