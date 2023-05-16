import sys
input = sys.stdin.readline


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.children = {}
        self.data = None

class Trie:

    def __init__(self):
        self.head = Node(None)

    def insert(self, string):

        current = self.head

        for char in string:

            if not char in current.children:
                current.children[char] = Node(char)
            current = current.children[char]

        current.data = string
        return True

    def start_with(self, string):
        current = self.head.children[string[0]]
        count = 1

        for char in string[1:]:

            if char in current.children:
                if len(current.children) == 1 and current.data == None:
                    current = current.children[char]
                else:
                    count += 1
                    current = current.children[char]

        return count

def solv():
    global total
    while True:
        total = 0
        n,words = input_data()
        if n == -1:
            break

        trie = Trie()
        for word in words:
            trie.insert(word)

        total = 0
        for word in words:
            total += trie.start_with(word)

        result = total / len(words)
        print(f"{round(result, 2):.2f}")
            
def input_data():
    try:
        n = int(input())
        words = [input().strip() for _ in range(n)]
        return n,words
    except:
        return -1,[]
solv()