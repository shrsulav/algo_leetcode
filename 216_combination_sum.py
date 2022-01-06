from typing import *
import copy
class Solution:
    def __init__(self) -> None:
        self.output = []
    def generate(self, candidates, target, t_list, k):
        if(target < 0):
            return
        
        if(target == 0 and len(t_list)==k):
            self.output.append(copy.deepcopy(t_list))
            return

        if(target ==0 and len(t_list) != k):
            return

        if(target != 0 and len(t_list) == k):
            return

        for index, num in enumerate(candidates):
            t_list.append(num)
            self.generate(candidates[index+1:], target-num, t_list, k)
            t_list.pop()

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.output = []
        candidates = [1,2,3,4,5,6,7,8,9]
        for index,num in enumerate(candidates):
            current = [num]
            self.generate(candidates[index+1:], n-num, current, k)
            
        return self.output
    

if __name__ == '__main__':
    soln = Solution()
    print(soln.combinationSum3(3,7))
    print(soln.combinationSum3(3,9))