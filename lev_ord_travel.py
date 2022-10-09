#time complexity: o(n)
#space complexity:o(1)
#passed all cases on LeetCode:yes
#difficulty faced:
# comments: in the code
#https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: 'Optional[TreeNode]') -> 'List[List[int]]':
        result = [] #2d list
        if root is None: return result
        q = []
        q.append(root)
        print(root.val)
        while q:
            size = len(q)
            #remem orig size bec it is gonna change
            l1 = []
            #use the above size
            for i in range(size):
                #pop from the left
                curr = q.pop(0)
                print(curr.val)
                l1.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            #after completing for loop append all the elements of the list        
            result.append(l1)
        return result




