from typing import *
import copy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        self.paths = 0
    def sum2(self, node, target, paths):
        for index in range(len(paths)-1):
            paths[index] += paths[-1]
        self.paths += paths.count(target)

        if(node == None):
            return

        if(node.left == None and node.right == None):
            return
        else:
            if(node.left != None):
                paths.append(node.left.val)
                self.sum2(node.left, target, paths)
                for index in range(len(paths)-1):
                    paths[index] -= paths[-1]
                paths.pop()
            
            if(node.right != None):
                paths.append(node.right.val)
                self.sum2(node.right, target, paths)
                for index in range(len(paths)-1):
                    paths[index] -= paths[-1]
                paths.pop()

            return
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if(root == None):
            return 0
        self.paths = 0
        self.sum2(root, targetSum, [root.val])
        return self.paths
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
        return self.pathSum(root, targetSum)

if(__name__ == '__main__'):
    soln = Solution()
    # input = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    # print(soln.hasPathSumList(input, 22))
    # print(soln.hasPathSumList([1,2,3], 5))
    # print(soln.hasPathSumList([], 0))
    print(soln.hasPathSumList([10,5,-3,3,2,None,11,3,-2,None,1], 8))
    print(soln.hasPathSumList([5,4,8,11,None,13,4,7,2,None,None,5,1], 22))
    print(soln.hasPathSumList([1],1))