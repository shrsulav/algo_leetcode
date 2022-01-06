from typing import *

class Solution:
    # submitted solution
    def jump4(self, nums, currentPos):
        if(currentPos == len(nums)-1):
            return 0
        table = [0]
        start = len(nums)-1
        end = -1
        goal = len(nums) - 1
        for pos in range(start, end, -1):
            maxJump = nums[pos]
            if(maxJump == 0):
                table.insert(0, float('inf'))
            elif(pos + maxJump >= goal):
                table.insert(0,1)
            else:
                jumps = 1 + min(table[:maxJump])
                table.insert(0,jumps)
        return table[0]
    
    def jump2(self, nums, currentPos, steps):
        if(currentPos == len(nums)-1):
            return steps
        
        if(nums[currentPos] == 0):
            return float('inf')

        minSteps = float('inf')
        for i in range(1, nums[currentPos]+1):
            currentSteps = self.jump2(nums, currentPos+i, steps+1)
            if(currentSteps < minSteps):
                minSteps = currentSteps
        
        return minSteps

    def jump(self, nums: List[int]) -> int:
        self.table = {}
        return self.jump4(nums, 0)

if(__name__ == '__main__'):
    soln = Solution()
    print(soln.jump([2,3,1,1,4]))
    print(soln.jump([2,3,0,1,4]))
    print(soln.jump([3,2,1,0,4]))
    print(soln.jump([2,1]))
    print(soln.jump([1,2,1,1,1]))
    print(soln.jump([0]))