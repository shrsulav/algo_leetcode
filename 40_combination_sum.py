from typing import *
import copy
class Solution:
    def __init__(self) -> None:
        self.output = []
    def generate(self, candidates, target, t_list):
        if(target < 0):
            return
        
        if(target == 0):
            self.output.append(copy.deepcopy(t_list))
            return

        lastCandidate = None
        for index, num in enumerate(candidates):
            if(lastCandidate == num):
                continue
            t_list.append(num)
            lastCandidate = num
            self.generate(candidates[index+1:], target-num, t_list)
            t_list.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.output = []
        candidates.sort()
        lastCandidate = None
        for index,num in enumerate(candidates):
            if(num == lastCandidate):
                continue
            current = [num]
            lastCandidate = num
            self.generate(candidates[index+1:], target-num, current)
            
        return self.output
    
if __name__ == '__main__':
    soln = Solution()
    print(soln.combinationSum([1,2,5], 5))
    print(soln.combinationSum([2,3,6,7], 7))
    print(soln.combinationSum([10,1,2,7,6,1,5, 5], 8))