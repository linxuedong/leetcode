class Solution:
    def isValidSudoku1(self, board):
        row = []
        col = []
        block = [
            [
                [], [], []
            ],
            [
                [], [], []
            ],
            [
                [], [], []
            ]
            
        ]

        for m in range(9):
            row.append(set())
            for n in range(9):

                if len(col) < 9:
                    col.append(set())

                num = board[m][n]

                if num == '.':
                    continue
                elif num not in row[m] and num not in col[n] and num not in block[m // 3][n // 3]:
                    row[m].add(num)
                    col[n].add(num)
                    block[m // 3][n // 3].append(num)
                else:
                    return False

        return True

    def isValidSudoku(self, board):
        row = [{} for _ in range(9)]
        col = [{} for _ in range(9)]
        block = [{} for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    row[i][num] = row[i].get(num, 0) + 1
                    col[j][num] = col[j].get(num, 0) + 1
                    index = i // 3 * 3 + j // 3
                    block[index][num] = block[index].get(num, 0) + 1
                    if row[i][num] > 1 or col[j][num] > 1 or block[index][num] > 1:
                        return False
        return True




                    
if __name__ == "__main__":
    lst1 = [
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

    res = Solution().isValidSudoku(lst1)

    assert res == True
