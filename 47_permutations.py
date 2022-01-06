from typing import *
import copy

# Runtime 62ms
class Solution:
    def __init__(self):
        self.paths = []
    def generate(self, nums, current):
        if(len(nums) == 0):
            done = copy.deepcopy(current)
            self.paths.append(done)
        t_nums = copy.deepcopy(nums)
        lastNum = None
        for index,num in enumerate(nums):
            if(num == lastNum):
                continue
            lastNum = num
            current.append(num)
            t_nums.pop(index)
            self.generate(t_nums, current) 
            t_nums.insert(index,num)
            current.pop()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.paths = []
        nums.sort()
        self.generate(nums, [])
        return self.paths

if __name__ == '__main__':
    soln = Solution()
    print(soln.permuteUnique([1,2,3]))
    print(soln.permuteUnique([0,1]))
    print(soln.permuteUnique([1]))
    print(soln.permuteUnique([1,1,2]))
    print(soln.permuteUnique([3,3,0,3]))