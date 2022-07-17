a_str = str(input().strip())

result = ''
for k in a_str:

    if ord(k) < 97:

        tmp = ord(k) + 32
        result += chr(tmp)
    else:
        tmp = ord(k) - 32
        result += chr(tmp)

print(''.join(result))