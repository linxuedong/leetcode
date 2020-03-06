class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            node = node.setdefault(char, {})  
        node['#'] = '#'

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return '#' in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]

        return True
    

if __name__ == "__main__":
    # Your Trie object will be instantiated and called as such:
    obj = Trie()
    obj.insert('apple')
    print(obj.root)
    param_2 = obj.search('apple')
    assert param_2 == True

    param_3 = obj.startsWith('app')
    assert param_3 == True

    assert obj.search('app') == False

