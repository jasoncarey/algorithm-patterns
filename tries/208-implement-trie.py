"""
208. Implement Trie (Prefix Tree)
https://leetcode.com/problems/implement-trie-prefix-tree/description/

Medium

TC: O(n)  # length of word
SC: O(t)  # number of total nodes
"""


class TrieNode:
    def __init__(self):
        self.children = {}  # each node contains a map to its children
        self.isEnd = False  # mark whether a node is the last letter of a word


class Trie:

    def __init__(self):
        self.root = TrieNode()  # entry point remains empty

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True

    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isEnd

    def starts_with(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


if __name__ == "__main__":
    trie = Trie()
    trie.insert("dog")
    print(f'output: {trie.search("dog")}, ans: True')
    print(f"output: {trie.search('do')}, ans: False")
    print(f'output: {trie.starts_with("do")}, ans: True')
    trie.insert("do")
    print(f'output: {trie.search("do")}, ans: True')
