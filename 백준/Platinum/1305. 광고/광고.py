import sys
input = sys.stdin.readline
L = int(input())
screen = str(input().rstrip())

def getMinPossibleLength(string):
    length = len(string)
    pi = [0] * (length)
    j = 0

    for i in range(1, length):
        while j > 0 and string[i] != string[j]:
            j = pi[j - 1]

        if string[i] == string[j]:
            j += 1
            pi[i] = j

    return L - pi[-1]

minPossibleLength = getMinPossibleLength(screen)
print(minPossibleLength)