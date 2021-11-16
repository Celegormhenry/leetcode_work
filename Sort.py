'''
剑指 Offer 45. 把数组排成最小的数
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

示例 1:

输入: [10,2]
输出: "102"
示例 2:

输入: [3,30,34,5,9]
输出: "3033459"

'''
#运用快排的思想，改变大小判断条件。时间复杂度O（logN）
class Solution:
    def minNumber(self, nums: List[int]) -> str:

        def quick_sort(l , r):
            if l >= r: return
            i, j = l, r
            while i < j:
                while i<j and strs[j]+strs[l]>=strs[l]+strs[j]: j-=1
                while i<j and strs[i]+strs[l]<=strs[l]+strs[i]: i+=1
                strs[i], strs[j] = strs[j], strs[i]
            strs[i], strs[l] = strs[l], strs[i]
            quick_sort(l, i - 1)
            quick_sort(i + 1, r)
        strs = [str(num) for num in nums]
        quick_sort(0, len(strs) - 1)
        return ''.join(strs)


'''
剑指 Offer 61. 扑克牌中的顺子
从若干副扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

示例 1:

输入: [1,2,3,4,5]
输出: True
 
示例 2:

输入: [0,0,1,2,5]
输出: True
'''
#先排序，再统计 时间复杂度O(nlogn)
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        if len(nums)<5:
            return False
        joker = 0
        nums.sort() # 数组排序
        for i in range(4):
            if nums[i] == 0: joker += 1 # 统计大小王数量
            elif nums[i] == nums[i + 1]: return False # 若有重复，提前返回 false
        return nums[4] - nums[joker] < 5 # 最大牌 - 最小牌 < 5 则可构成顺子

'''
剑指 Offer 40. 最小的k个数
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]
'''
#快排：
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        def quicksort(arr, l, r):
            if l >= r: return
            start = l
            end = r
            mid = arr[l]
            while l < r:
                while l < r and arr[r] >= mid: r -= 1
                while l < r and arr[l] <= mid: l += 1

                arr[l], arr[r] = arr[r], arr[l]
            arr[start], arr[l] = arr[l], arr[start]
            quicksort(arr, start, l - 1)
            quicksort(arr, l + 1, end)

        quicksort(arr, 0, len(arr) - 1)
        return arr[:k]

#运用快排思想，在快排中比较k和左右数组的数量：时间复杂度是 N + N/2 + N/4 + ... + N/N = 2N, 因此时间复杂度是 O(N)。
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k >= len(arr): return arr

        def quicksort(arr, l, r):
            if l >= r: return
            start = l
            end = r
            mid = arr[l]
            while l < r:
                while l < r and arr[r] >= mid: r -= 1
                while l < r and arr[l] <= mid: l += 1

                arr[l], arr[r] = arr[r], arr[l]
            arr[start], arr[l] = arr[l], arr[start]
            if k < l: quicksort(arr, start, l - 1)
            if k > l: quicksort(arr, l + 1, end)

        quicksort(arr, 0, len(arr) - 1)
        return arr[:k]
#也可以用堆和二叉树来解决

'''
剑指 Offer 41. 数据流中的中位数
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例 1：

输入：
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
输出：[null,null,null,1.50000,null,2.00000]
'''
#用两个堆来做，一个存小的一半，一个存大的一半
from heapq import *
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.big = []

    def addNum(self, num: int) -> None:
        if len(self.small)==len(self.big):
            heappush(self.small, -num)
            heappush(self.big, -heappop(self.small))
        else:
            heappush(self.big, num)
            heappush(self.small, -heappop(self.big))

    def findMedian(self) -> float:
        if len(self.small)==len(self.big):
            return (-self.small[0] + self.big[0]) / 2.0
        else:
            return self.big[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
