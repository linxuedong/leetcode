d_x = [-1, 0, 1, 0]
d_y = [0, -1, 0, 1]

END_OF_WORD = "#"

from collections import defaultdict

class Solution:
    def findWords(self, board, words):
        self.m = len(board)
        self.n = len(board[0])

        root = self.trie(words)
        self.result = set()

        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in root:
                    marked = [[False for _ in range(self.n)] for _ in
                              range(self.m)]
                    self.search_word(board, i, j, marked, root, '')

        return list(self.result)

    def search_word(self, board, i, j, marked, node, word):
        char = board[i][j]
        word += char
        node = node[char]
        marked[i][j] = True

        if END_OF_WORD in node:
            self.result.add(word)

        for index in range(4):
            new_i = i + d_x[index]
            new_j = j + d_y[index]

            if 0 <= new_i < self.m and 0 <= new_j < self.n and board[new_i][new_j] in node and not marked[new_i][new_j]:
                self.search_word(board, new_i, new_j, marked, node, word)
        marked[i][j] = False

    def trie(self, words):
        root = defaultdict(dict)
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char, defaultdict())
            node[END_OF_WORD] = END_OF_WORD
        return root

if __name__ == "__main__":
    board = [["b", "a", "a", "b", "a", "b"], ["a", "b", "a", "a", "a", "a"],
     ["a", "b", "a", "a", "a", "b"], ["a", "b", "a", "b", "b", "a"],
     ["a", "a", "b", "b", "a", "b"], ["a", "a", "b", "b", "b", "a"],
     ["a", "a", "b", "a", "a", "b"]]
    words = ["bbaabaabaaaaabaababaaaaababb","aabbaaabaaabaabaaaaaabbaaaba","babaababbbbbbbaabaababaabaaa","bbbaaabaabbaaababababbbbbaaa","babbabbbbaabbabaaaaaabbbaaab","bbbababbbbbbbababbabbbbbabaa","babababbababaabbbbabbbbabbba","abbbbbbaabaaabaaababaabbabba","aabaabababbbbbbababbbababbaa","aabbbbabbaababaaaabababbaaba","ababaababaaabbabbaabbaabbaba","abaabbbaaaaababbbaaaaabbbaab","aabbabaabaabbabababaaabbbaab","baaabaaaabbabaaabaabababaaaa","aaabbabaaaababbabbaabbaabbaa","aaabaaaaabaabbabaabbbbaabaaa","abbaabbaaaabbaababababbaabbb","baabaababbbbaaaabaaabbababbb","aabaababbaababbaaabaabababab","abbaaabbaabaabaabbbbaabbbbbb","aaababaabbaaabbbaaabbabbabab","bbababbbabbbbabbbbabbbbbabaa","abbbaabbbaaababbbababbababba","bbbbbbbabbbababbabaabababaab","aaaababaabbbbabaaaaabaaaaabb","bbaaabbbbabbaaabbaabbabbaaba","aabaabbbbaabaabbabaabababaaa","abbababbbaababaabbababababbb","aabbbabbaaaababbbbabbababbbb","babbbaabababbbbbbbbbaabbabaa"]
    print(Solution().findWords(board, words))

