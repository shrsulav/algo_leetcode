from typing import *

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        accum = 0
        rem = 0
        output = 0
        rem_map = {0:1}
        for num in nums:
            accum += num
            rem = accum % k

            if(rem in rem_map):
                output += rem_map[rem]
 
            if(rem in rem_map):
                rem_map[rem] += 1
            else:
                rem_map[rem] = 1
        return output

if __name__ == '__main__':
    soln = Solution()
    # print(soln.subarraysDivByK([4,5,0,-2,-3,1], 5))
    # print(soln.subarraysDivByK([5], 9))
    print(soln.subarraysDivByK([8,9,7,8,9], 8))