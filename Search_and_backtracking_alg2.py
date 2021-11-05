'''
剑指 Offer 26. 树的子结构
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：

输入：A = [1,2,3], B = [3,1]
输出：false
示例 2：

输入：A = [3,4,5,1,2], B = [4,1]
输出：true
'''
#二叉树dfs,需要做两遍
#1.先序遍历树 A中的每个节点，是否与B相等
#2.判断树 A 中 以 nA 为根节点的子树 是否包含树 B

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:

        def helper(nodeA, nodeB):
            if not nodeB:
                return True
            if not nodeA or nodeA.val != nodeB.val:
                return False
            return helper(nodeA.left, nodeB.left) and helper(nodeA.right, nodeB.right)

        def dfs(nodeA, nodeB):
            if not nodeA: return False
            if not nodeB: return False
            if nodeA.val == nodeB.val:
                if helper(nodeA, nodeB):
                    return True
            return dfs(nodeA.left, nodeB) or dfs(nodeA.right, nodeB)

        return dfs(A, B)

'''
剑指 Offer 27. 二叉树的镜像
请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
镜像输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

示例 1：

输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
'''
#dfs递归遍历
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        tmp = root.left
        root.left = self.mirrorTree(root.right)
        root.right = self.mirrorTree(tmp)
        return root

'''
剑指 Offer 28. 对称的二叉树
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

示例 1：

输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：

输入：root = [1,2,2,null,3,null,3]
输出：false
'''
#递归遍历二叉树

# 做递归思考三步：
#
# 递归的函数要干什么？
# 函数的作用是判断传入的两个树是否镜像。
# 输入：TreeNode left, TreeNode right
# 输出：是：true，不是：false
# 递归停止的条件是什么？
# 左节点和右节点都为空 -> 倒底了都长得一样 ->true
# 左节点为空的时候右节点不为空，或反之 -> 长得不一样-> false
# 左右节点值不相等 -> 长得不一样 -> false
# 从某层到下一层的关系是什么？
# 要想两棵树镜像，那么一棵树左边的左边要和二棵树右边的右边镜像，一棵树左边的右边要和二棵树右边的

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(left,right):
            if not left and not right: return True
            if not left or not right or left.val != right.val: return False
            return dfs(left.left,right.right) and dfs(left.right,right.left)
        return dfs(root.left,root.right) if root else True