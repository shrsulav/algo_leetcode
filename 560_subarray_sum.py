from typing import *

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # if(len(nums) == 0):
        #     return 0
        # if(len(nums) == 1):
        #     if(nums[0] == k):
        #         return 1
        #     else:
        #         return 0
        prefix_sum = {0:1}
        p_sum = 0
        output = 0
        for num  in nums:
            p_sum += num
            if(p_sum-k in prefix_sum):
                output += prefix_sum[p_sum-k]
            if(p_sum in prefix_sum):
                prefix_sum[p_sum] += 1
            else:
                prefix_sum[p_sum] = 1

        return output

if __name__ == '__main__':
    soln = Solution()
    print(soln.subarraySum([1,2,3],3))
    print(soln.subarraySum([1],0))
    print(soln.subarraySum([-1, -1, 1],0))
