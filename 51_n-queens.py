class Solution:
    def solveNQueens(self, n):
        self.column = []; self.left = set(); self.right = set()
        self.result = []
        self.get_result(n, 0)
        return self._generate_result(n)

    def _generate_result(self, n):
        board = []
        for r in self.result:
            board.append([])
            for col in r:
                board[-1].append('.'*col + 'Q' + '.'* (n -col-1))
        return board

    def get_result(self, n, level):
        if level == n:
            self.result.append(self.column.copy())
            return 

        for i in range(n):
            if i in self.column \
                or level + i in self.left \
                or i - level in self.right:
                continue
                
            self.column.append(i)
            self.left.add(level + i)
            self.right.add(i - level)

            self.get_result(n, level+1)

            self.column.remove(i)
            self.left.remove(level + i)
            self.right.remove(i - level)


class Solution2:
    def solveNQueens(self, n):
        self.result = []
        self.n = n
        self.dfs([], [], [])
        return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in self.result]

    def dfs(self, column, left, right):
        level = len(column)
        if self.n == level:
            self.result.append(column.copy())
            return
        
        for i in range(self.n):
            if i in column \
                or level + i in left \
                or i - level in right:
                continue

            self.dfs(column+[i], 
                     left+[level + i], 
                     right+[i - level])
                





if __name__ == "__main__":
    a  = Solution2().solveNQueens(4)
    print(a)