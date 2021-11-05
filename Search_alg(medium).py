'''
剑指 Offer 04. 二维数组中的查找
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

示例:

现有矩阵 matrix 如下：
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。

限制：

0 <= n <= 1000

0 <= m <= 1000
'''
#通过找规律，从左下角开始找起，小于target就右移，大于target则上移。 时间复杂度：O(M+N)
class Solution:
    def findNumberIn2DArray(self, matrix, target):
        if not matrix: return False
        m, n = len(matrix), len(matrix[0])
        row, col = m - 1, 0
        while row >= 0 and col < n:
            if matrix[row][col] < target:
                col += 1
            elif matrix[row][col] > target:
                row -= 1
            else:
                return True
        return False

'''
剑指 Offer 11. 旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0
'''
#二分查找 时间复杂度由于有重复数字，所以最坏O(n)
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        if not numbers:
            return 0
        start, end = 0, len(numbers) - 1
        while start < end:
            mid = (start + end) // 2
            if numbers[mid]>numbers[end]:
                start = mid+1
            elif numbers[mid] < numbers[end]:
                end = mid
            else:
                end-=1
        return min(numbers[start],numbers[end])

'''
剑指 Offer 50. 第一个只出现一次的字符
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例 1:

输入：s = "abaccdeff"
输出：'b'
示例 2:

输入：s = "" 
输出：' '
'''
#哈希表遍历两次
class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = collections.OrderedDict()
        for c in s:
            dic[c] = not c in dic
        for k, v in dic.items():
            if v: return k
        return ' '
