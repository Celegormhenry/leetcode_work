'''
12. 矩阵中的路径
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。

示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false

'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        dirs = [[0,1], [0,-1], [1,0],[-1,0]]
        def dfs(x, y, idx):
            if not 0 <= x < m or not 0 <= y < n or visited[x][y] == 1 or board[x][y] != word[idx]:
                return False
            if idx == len(word)-1:
                return True
            visited[x][y] = 1
            for i,j in dirs:
                if dfs(x+i, y+j, idx+1):
                    return True
            visited[x][y] = 0
            return False

        visited = [[0]*n for k in range(m)]
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i,j,k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j]!=word[k]:
                return False
            if  k == len(word) - 1:
                return True
            board[i][j] = ''
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = word[k]
            return res
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
        return False

'''
剑指 Offer 13. 机器人的运动范围
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
'''
#dfs
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = [[0]*n for k in range(m)]
        def sumx(x):
            ans = 0
            while x:
                ans += x % 10
                x //= 10
            return ans
        def dfs(i,j):
            if not 0<=i<m or not 0<=j<n or visited[i][j] or (sumx(i)+sumx(j))>k:
                return 0
            visited[i][j] = 1
            res = 1 + dfs(i+1,j) + dfs(i,j+1) + dfs(i-1,j) + dfs(i,j-1)
            return res
        return dfs(0,0)

#bfs
def digitsum(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        from queue import Queue
        q = Queue()
        q.put((0, 0))
        s = set()
        while not q.empty():
            x, y = q.get()
            if (x, y) not in s and 0 <= x < m and 0 <= y < n and digitsum(x) + digitsum(y) <= k:
                s.add((x, y))
                for nx, ny in [(x + 1, y), (x, y + 1)]:
                    q.put((nx, ny))
        return len(s)
