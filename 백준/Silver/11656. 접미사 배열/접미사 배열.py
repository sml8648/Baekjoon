n = str(input().strip())

result = []
for i in range(len(n)):

    result.append(n[i:])

print('\n'.join(sorted(result)))
