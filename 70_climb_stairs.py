from typing import *

class Solution:
    def climbStairs(self, n: int) -> int:
        if(n == 1):
            return 1
        if(n == 2):
            return 2
        # output = self.climbStairs(n-1) + self.climbStairs(n-2)

        dp = [1,2]
        for i in range(2, n):
            dp.append(dp[i-1] + dp[i-2])
        return dp[-1]