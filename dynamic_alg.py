'''
剑指 Offer 10- I. 斐波那契数列
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：1
示例 2：

输入：n = 5
输出：5
'''
#简单动态规划
class Solution:
    def fib(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        if n < 2:
            return n
        x1, x2, r = 0, 0, 1
        for i in range(2, n+1):
            x1 = x2
            x2 = r
            r = (x1+x2)%MOD
        return r

'''
剑指 Offer 10- II. 青蛙跳台阶问题
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2
示例 2：

输入：n = 7
输出：21
示例 3：

输入：n = 0
输出：1
'''
class Solution:
    def numWays(self, n: int) -> int:
        MOD = 10**9+7
        if n < 2:
            return 1
        x1 = 1
        x2 = 1
        for i in range(2, n+1):
            r = (x1+x2)%MOD
            x1 = x2
            x2 = r
        return r

'''
剑指 Offer 63. 股票的最大利润
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
'''
#动态规划，维护一个最小buyin，时间复杂度O(n),可优化存储空间到O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        buyin = prices[0]
        n = len(prices)
        dp = 0
        for i in range(1,n):
            buyin = min(buyin,prices[i])
            dp = max(dp,prices[i]-buyin)
        return dp

'''
剑指 Offer 42. 连续子数组的最大和
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
'''
#动态规划
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = 0
        output = nums[0]
        for i in range(1,n+1):
            dp = max(nums[i-1], dp + nums[i-1])
            output = max(output,dp)
        return output
#另外可以用分治方法，是线段树的雏形
# nums[low, high]的任何连续子数组nums[i, j]
# 所处的位置必位于3种情况下：
# 1 位于nums[low, mid]
# 2 位于nums[mid + 1, high]
# 3 跨越中点mid, low <= i <= mid < j <= high
# 前两种情况是规模更小的原问题
# 第三种情况非规模更小的原问题，因为加入了限制（子数组跨越中点），对该情况的处理思路为：
# 拆分原来数组为nums[i, mid], nums[mid + 1, j], 分别找出最大子数组再进行合并。
# 当n > 1时，时间运行时间T(n) = 2T(n / 2) + O(n), 结果是T(n) = O(nlogn)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 处理子数组跨越中点的情况
        def findcross(nums, low, mid, high):
            left_sum, temp_sum = float("-inf"), 0
            for i in range(mid, low - 1, -1):
                temp_sum += nums[i]
                if temp_sum > left_sum:
                    left_sum = temp_sum
                    max_left = i

            right_sum, temp_sum = float("-inf"), 0
            for j in range(mid + 1, high + 1):
                temp_sum += nums[j]
                if temp_sum > right_sum:
                    right_sum = temp_sum
                    max_right = j

            return max_left, max_right, left_sum + right_sum

        def findmaxmin(nums, low, high):
            if low == high:
                return low, high, nums[low]
            else:
                mid = (low + high) // 2
                left_low, left_high, left_sum = findmaxmin(nums, low, mid)
                right_low, right_high, right_sum = findmaxmin(nums, mid + 1, high)
                cross_low, cross_high, cross_sum = findcross(nums, low, mid, high)
            # 取那些最大
            if left_sum >= right_sum and left_sum >= cross_sum:
                return (left_low, left_high, left_sum)
            elif right_sum >= left_sum and right_sum >= cross_sum:
                return (right_low, right_high, right_sum)
            else:
                return (cross_low, cross_high, cross_sum)

        return findmaxmin(nums, 0, len(nums) - 1)[2]

'''
剑指 Offer 47. 礼物的最大价值
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

示例 1:

输入: 
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物'''
#动态规划，用原有数组节省存储空间
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        #dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if i > 0 and j >0:
                    grid[i][j] = max(grid[i-1][j],grid[i][j-1])+grid[i][j]
        return grid[-1][-1]

'''
剑指 Offer 46. 把数字翻译成字符串
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
'''
#动规，转移方程：f(i)=f(i−1)+f(i−2)[i−1≥0,10≤x≤25]
class Solution:
    def translateNum(self, num: int) -> int:
        nums = str(num)
        n = len(str(num))
        dp = [1]*(n+1)
        for i in range(2,n+1):
            if "10" <= nums[i - 2:i] <= "25" :
                dp[i] = dp[i-1]+dp[i-2]
            else:
                dp[i] = dp[i-1]
        return dp[-1]

'''
剑指 Offer 48. 最长不含重复字符的子字符串
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

 

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''
#可以用双指针滑动窗口的方法，时间复杂度O(n^2)，加上哈希表O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        hashmap = {}
        head, res = 0, 0
        for tail in range(n):
            if s[tail] in hashmap:
                head = max(hashmap[s[tail]], head)
            hashmap[s[tail]] = tail + 1
            res = max(res, tail - head + 1)
        return res


#动态规划加哈希表存储最后出现位置，O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        dp = 0
        maxl = 0
        sdict = {}
        for i in range(n):
            j = sdict.get(s[i], -1)  # 获取索引 i
            sdict[s[i]] = i
            if i - j > dp:
                dp += 1
            else:
                dp = i - j

            maxl = max(maxl, dp)
        return maxl
