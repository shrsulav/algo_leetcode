from typing import *
import copy
class Solution:
    def __init__(self) -> None:
        self.table = {0:1}

    def combinationSum4(self, candidates: List[int], target: int) -> List[List[int]]:
        if(target == 0):
            return 1
        if(target < 0):
            return 0
        if target in self.table:
            return self.table[target]

        for curr_target in range(1, target+1):
            ways = 0
            for num in candidates:
                ways += self.combinationSum4(candidates, curr_target - num)
            self.table[curr_target] = ways
        
        output = self.table[target]
        self.table = {0:1}
        return output
     
if __name__ == '__main__':
    soln = Solution()
    print(soln.combinationSum4([1,2,3], 4))
    
    print(soln.combinationSum4([9], 3))
    print(soln.combinationSum4([4,2,1], 32))