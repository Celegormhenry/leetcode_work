'''
剑指 Offer 03. 数组中重复的数字
找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3
'''
#最简单用哈希表，这个方法是原地交换利用数组元素的索引和值是 一对多 的关系。
#因此，可遍历数组并通过交换操作，使元素的 索引 与 值 一一对应（即 nums[i] = inums[i]=i ）。因而，就能通过索引映射对应的值，起到与字典等价的作用。

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            elif nums[nums[i]]==nums[i]:
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1

'''
剑指 Offer 53 - I. 在排序数组中查找数字 I
统计一个数字在排序数组中出现的次数。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
'''
#最简单的方法还是哈希表，但我用了两个二分法分别左右逼近target在排序数组中的位置。时间复杂度： O(logn)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        left, right = -1, -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            right = start
        if nums[end] == target:
            right = end

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        if nums[end] == target:
            left = end
        if nums[start] == target:
            left = start
        if left == -1 and right == -1:
            return 0
        return right - left + 1

'''
剑指 Offer 53 - II. 0～n-1中缺失的数字
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

示例 1:

输入: [0,1,3]
输出: 2
示例 2:

输入: [0,1,2,3,4,5,6,7,9]
输出: 8
'''
#二分查找
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == mid:
                left = mid+1
            else:
                right = mid-1

        return left