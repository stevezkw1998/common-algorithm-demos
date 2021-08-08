class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.isword = False
    
class TrieTree:
    def __init__(self):
        self.root = TrieNode("*")

    def add(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode(letter)
            curr = curr.children[letter]
        curr.isword = True
    
    def search(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return curr.isword

    def searchPrefix(self, prefix):
        curr = self.root
        for letter in prefix:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return curr.children != {}