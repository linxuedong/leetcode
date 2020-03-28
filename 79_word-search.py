# 79. 单词搜索
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

# 示例:
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false

class Solution1:
    def exist(self, board, word: str) -> bool:
        def _search_word(board, word, index, start_x, start_y, marked, m, n):
            # 递归终止条件
            if index == len(word) - 1:
                return board[start_x][start_y] == word[index]

            if board[start_x][start_y] == word[index]:
                marked[start_x][start_y] = True
                for i, j in _get_neighbor(start_x, start_y):
                    if not marked[i][j] and _search_word(board, word, index + 1,
                                                         i, j, marked, m,
                                                         n) == True:
                        return True

                marked[start_x][start_y] = False

            return False

        def _get_neighbor(r, c):
            """ 返回该坐标点的邻居坐标 """
            for nr, nc in (r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1):
                if 0 <= nr < Row and 0 <= nc < Col:
                    yield nr, nc

        if not board or not word: return False
        Row = len(board)
        Col = len(board[0])
        marked = [[False for _ in range(Col)] for _ in range(Row)]

        for i in range(Row):
            for j in range(Col):
                if _search_word(board, word, 0, i, j, marked, Row, Col):
                    return True

        return False


class Solution:

    def exist(self, board, word):
        if not board or not word: return 0

        start = word[0]
        self.m = len(board)
        self.n = len(board[0])
        self.direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()

        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == start:
                    visited.add((i, j))
                    if self.search(board, word[1:], visited, i, j):
                        return True

        return False

    def search(self, board, word, visited, i, j):
        # 字符为空则找完所有字符
        if not word:
            return True

        for k in range(4):
            ni = self.direction[k][0] + i
            nj = self.direction[k][1] + j

            if 0 <= ni < self.m and 0 <= nj < self.n and (ni, nj) not in visited and board[ni][nj] == word[0]:
                visited.add((ni, nj))
                if self.search(board, word[1:], visited, ni, nj): return True
        visited.remove((i, j))
        return False


if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = 'ABCD'

    assert Solution().exist(board, word) == False
    assert Solution().exist(board, 'ABCCED') == True

    board = [["C","A","A"],["A","A","A"],["B","C","D"]]
    assert Solution().exist(board, 'AAB')
