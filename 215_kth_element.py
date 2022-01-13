from typing import *

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        current = 0
        target = len(nums) - k
        k_partition = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i]< k_partition[current]:
                k_partition.insert(0, nums[i])
            else:
                k_partition.append(nums[i])
            if(len(k_partition) <= target):
                current = len(k_partition) - 1
            else:
                current = target
            
        return k_partition[target]

if __name__ == '__main__':
    soln = Solution()
    # print(soln.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
    # print(soln.findKthLargest([3,2,1,5,6,4], 2))
    print(soln.findKthLargest([-1,2,0], 2))