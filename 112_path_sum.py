from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sum2(self, node, target):
        # print(node.val)
        if(node == None):
            return False
        if(node.left == None and node.right == None):
            # print("Remainder is ", target-node.val)
            if(target - node.val == 0):
                return True
            else:
                return False
        else:
            sum_left = self.sum2(node.left, target - node.val)
            if(sum_left):
                return True
            sum_right = self.sum2(node.right, target - node.val)
            if(sum_right):
                return True

            return False
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.sum2(root, targetSum)
    
    def createTreeFromList(self, tree):
        if(len(tree) == 0):
            return None
        root = None
        for index in tree:
            if(index == 0):
                root = TreeNode(tree[0])
            else:
                treeIndex = index + 1
                parent = int(treeIndex / 2)
        return root
    # Function to insert nodes in level order
    def insertLevelOrder(self, arr, root, i, n):
         
        # Base case for recursion
        if i < n:
            temp = TreeNode(arr[i])
            root = temp
    
            # insert left child
            if((2*i+1) < len(arr) and arr[2*i + 1] != None):
                root.left = self.insertLevelOrder(arr, root.left, 2 * i + 1, n)
    
            # insert right child
            if((2*i+1) < len(arr) and arr[2*i + 2] != None):
                root.right = self.insertLevelOrder(arr, root.right, 2 * i + 2, n)
        return root
    def hasPathSumList(self, tree, targetSum):
        # root = self.createTreeFromList(tree)
        root = None
        root = self.insertLevelOrder(tree, root, 0, len(tree))
        return self.hasPathSum(root, targetSum)

if(__name__ == '__main__'):
    soln = Solution()
    input = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    print(soln.hasPathSumList(input, 22))
    print(soln.hasPathSumList([1,2,3], 5))
    print(soln.hasPathSumList([], 0))