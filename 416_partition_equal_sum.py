from typing import *

class Solution:
    def knapsack(self, target, nums):
        table = [[0 for x in range(target + 1)] for x in range(len(nums) + 1)]
        for i in range(len(nums)+1):
            for t_target in range(target+1):
                if i==0 or t_target==0:
                    table[i][t_target] = 0
                elif nums[i-1] <= t_target:
                    table[i][t_target] = max(nums[i-1] + table[i-1][t_target-nums[i-1]], table[i-1][t_target])
                else:
                    table[i][t_target] = table[i-1][t_target]
            if(table[i][target] == target):
                return True

        if(table[-1][-1] == target):
            return True
        else:
            return False

    # does not work
    def subsetSum(self, target, nums):
        table = [True]
        for i in range(target):
            table.append(False)
        
        for num in nums:
            for current_target in range(target+1):
                table[current_target] = table[current_target] or table[current_target - num]

        return table[-1]
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if(total%2 != 0):
            return False
        
        return self.knapsack(int(total/2), nums)

if __name__ == '__main__':
    soln = Solution()
    print(soln.canPartition([1,5,11,5]))
    print(soln.canPartition([1,2,3,5]))
    print(soln.canPartition([3,3,3,4,5]))
    print(soln.canPartition([1,2,5]))