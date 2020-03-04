from collections import defaultdict
class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def could_place(d, row, col):
            """
            检查数字 d 能否填入空格 (row, col)
            """
            return d not in rows[row] and d not in cols[col] and d not in boxes[box_index(row, col)]

        def place_number(d, row, col):
            """
            在 (row, col) 防止数字 d
            """
            rows[row][d] += 1
            cols[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            board[row][col] = str(d)
            
        def remove_number(d, row, col):
            """
            将数值从 (row, col) 移除
            """
            del rows[row][d]
            del cols[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = '.'
        
        def place_next_numbers(row, col):
            """
            Call backtrack function in recursion
            to continue to place numbers
            till the moment we have a solution
            """
            # 完成数独
            if row + 1 == N and col + 1 == N:
                self.sudoku_sloved = True
            # 当前行完成，移动到下一行
            elif col + 1 == N:
                backtrack(row + 1, 0)
            # 移动到下一格
            else:
                backtrack(row, col + 1)
                
        def backtrack(row, col):
            """
            Backtracking
            """
            if board[row][col] == '.':
                # 遍历 数字 1 - 9
                for d in range(1, N+1):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_numbers(row, col)

                        if not self.sudoku_sloved:
                            remove_number(d, row, col)

            else:
                # 当前空格已填入数字，填入下一格
                place_next_numbers(row, col)

        n = 3
        N = n * n

        # 小 9 宫格的索引计算
        # 0 1 2
        # 3 4 5
        # 6 7 8
        box_index = lambda row, col: (row // n) * 3 + col // n

        # 已经存在个数值
        rows = [defaultdict(int) for _ in range(N)]
        cols = [defaultdict(int) for _ in range(N)]
        boxes = [defaultdict(int) for _ in range(N)]
        
        # 遍历数据，将已有数数字填入 rows, cols, boxes
        for r in range(N):
            for j in range(N):
                num = board[r][j]
                if num != '.':
                    num = int(num)
                    place_number(num, r, j)

        # 是否完成 数独
        self.sudoku_sloved = False

        # 从第一格开始解数独
        backtrack(0, 0)

            
if __name__ == "__main__":
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    Solution().solveSudoku(board)
    print(board)

