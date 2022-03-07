'''
21.
调整数组顺序使奇数位于偶数前面
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。
示例：

输入：nums = [1, 2, 3, 4]
输出：[1, 3, 2, 4]
注：[3, 1, 2, 4]
也是正确的答案之一。
'''
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        while left < right:
            while left < right and nums[left]%2==1: left+=1
            while left < right and nums[right]%2==0:right-=1
            nums[left],nums[right]=nums[right],nums[left]
        return nums

'''
57.
和为s的两个数字
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。
示例
1：

输入：nums = [2, 7, 11, 15], target = 9
输出：[2, 7]
或者[7, 2]
示例
2：

输入：nums = [10, 26, 30, 31, 47, 60], target = 40
输出：[10, 30]
或者[30, 10]
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        while left < right:
            if nums[left]+nums[right]>target:
                right-=1
            elif nums[left]+nums[right]<target:
                left+=1
            else:
                return [nums[left],nums[right]]
        return []


'''
58 - I.翻转单词顺序
输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。例如输入字符串
"I am a student. "，则输出
"student. a am I"。

示例
1：

输入: "the sky is blue"
输出: "blue is sky the"
示例
2：

输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
示例
3：

输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip() # 删除首尾空格
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ': i -= 1 # 搜索首个空格
            res.append(s[i + 1: j + 1]) # 添加单词
            while s[i] == ' ': i -= 1 # 跳过单词间空格
            j = i # j 指向下个单词的尾字符
        return ' '.join(res) # 拼接并返回

