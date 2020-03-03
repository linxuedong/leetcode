class Solution:
    def merge(self, A, m, B, n) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        A[m: m+n] = B
        A.sort()
        
    def merge1(self, A, m, B, n) -> None:
        sorted = []
        pa, pb = 0, 0
        while pa < m or pb < n:
            if pa == m:
                sorted.append(B[pb])
                pb += 1
            elif pb == n:
                sorted.append(A[pa])
                pa +=  1
            elif A[pa] > B[pb]:
                sorted.append(B[pb])
                pb += 1
            else:
                sorted.append(A[pa])
                pa += 1

        A[:] = sorted
        

if __name__ == "__main__":
    A = [1,2,3,0,0,0]
    m = 3
    B = [4,5,6]
    n = 3
    Solution().merge1(A, m, B, n)
    print(A)
    assert A == [1,2,3,4,5,6]


    A = [1]
    m = 1
    B = []
    n = 0
    Solution().merge1(A, m, B, n)
