class Solution:
    def generateParenthesis(self, n):
        if n <= 0: return []
        self.list = []
        self.helper(0, 0, n, '')
        return self.list
        
    def helper(self, left, right, n, result):
        if left == n and right == n:
            self.list.append(result)
        
        if left < n:
            self.helper(left+1, right, n, result + '(')

        if right < n and right < left:
            self.helper(left, right+1, n, result + ')')