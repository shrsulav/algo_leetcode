# from typing import *

class Solution:
    def twoSum(self, nums, target):
        entry_table = {}
        for index, num in enumerate(nums):
            if(target-num in entry_table):
                return [entry_table[target-num], index]
            entry_table[num] = index
        return None
if __name__ == '__main__':
    soln = Solution()
    print(soln.twoSum([1,2,3,4,5], 6))