import sys
input = sys.stdin.readline


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.children = {}


class Trie:

    def __init__(self):
        self.head = Node(None)

    def insert(self, string):

        current = self.head

        for char in string:

            if not char in current.children:
                current.children[char] = Node(char)
            current = current.children[char]

n = int(input())
trie = Trie()

for _ in range(n):
    tmp = list(input().split())
    num = int(tmp[0])
    insert_list = tmp[1:]

    trie.insert(insert_list)

def child_print(node, idx):

    children = node.children
    new_children = sorted(children.items())

    for each in new_children:
        print('-'*(idx)+each[0])
        child_print(each[1],idx+2)

head = trie.head
child_print(head, 0)