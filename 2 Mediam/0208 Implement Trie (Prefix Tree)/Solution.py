from collections import defaultdict

class TrieNode(object):
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            curr = curr.nodes[char]
        curr.isEnd = True

    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return curr.isEnd

    def startsWith(self, prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return True