from typing import *
import copy
# Runtime 62ms
class Solution:
    def __init__(self):
        self.paths = []
        self.current = []

    def generate(self, nums):
        if(len(nums) == 0):
            done = copy.deepcopy(self.current)
            self.paths.append(done)
        t_nums = copy.deepcopy(nums)
        for index,num in enumerate(nums):
            self.current.append(num)
            t_nums.pop(index)
            self.generate(t_nums) 
            t_nums.insert(index,num)
            self.current.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.paths = []
        self.current = []
        self.generate(nums)
        return self.paths

# Runtime 62ms
# class Solution:
#     def __init__(self):
#         self.paths = []
#     def generate(self, nums, current):
#         if(len(nums) == 0):
#             done = copy.deepcopy(current)
#             self.paths.append(done)
#         t_nums = copy.deepcopy(nums)
#         for index,num in enumerate(nums):
#             current.append(num)
#             t_nums.pop(index)
#             self.generate(t_nums, current) 
#             t_nums.insert(index,num)
#             current.pop()

#     def permute(self, nums: List[int]) -> List[List[int]]:
#         self.paths = []
#         self.generate(nums, [])
#         return self.paths

# Runtime 105ms
# class Solution:
#     def __init__(self):
#         self.paths = []
#     def generate(self, nums, current):
#         if(len(nums) == 0):
#             self.paths.append(current)
#         t_nums = copy.deepcopy(nums)
#         for index,num in enumerate(nums):
#             new_path = copy.deepcopy(current)
#             new_path.append(num)
#             t_nums.pop(index)
#             self.generate(t_nums, new_path) 
#             t_nums.insert(index,num)

#     def permute(self, nums: List[int]) -> List[List[int]]:
#         self.paths = []
#         self.generate(nums, [])
#         return self.paths
if __name__ == '__main__':
    soln = Solution()
    print(soln.permute([1,2,3]))
    print(soln.permute([0,1]))
    print(soln.permute([1]))