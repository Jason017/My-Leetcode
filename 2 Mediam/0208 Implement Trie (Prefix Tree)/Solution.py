from collections import defaultdict

class TrieNode:
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

def main():
    t = Trie()
    t.insert("apple")
    print(t.search("apple")) # True
    print(t.search("app")) # False
    print(t.startsWith("app")) # True
    t.insert("app")
    print(t.search("app")) # True

if __name__ == "__main__":
    main()
