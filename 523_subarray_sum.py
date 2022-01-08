from typing import *

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        r_map = {0:-1}
        t_sum = 0
        for i in range(len(nums)):
            t_sum += nums[i]
            rem = t_sum % k
            if(rem in r_map):
                if i - r_map[rem] > 1:
                    return True
            else:
                r_map[rem] = i

        return False
    

if __name__ == '__main__':
    soln = Solution()
    print(soln.checkSubarraySum([23,2,4,6,6], 7))