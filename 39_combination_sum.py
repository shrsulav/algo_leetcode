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

        for index, num in enumerate(candidates):
            t_list.append(num)
            self.generate(candidates[index:], target-num, t_list)
            t_list.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.output = []
        for index,num in enumerate(candidates):
            current = [num]
            self.generate(candidates[index:], target-num, current)
        
        return self.output
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        table = []
        row = [1]
        for i in range(target):
            row.append(0)
        
        table.append(row)
        for index,num in enumerate(candidates):
            row = [1]
            for curr_target in range(target):
                ways = 0
                if(num <= i):
                    ways = row[curr_target-num] + table[index-1][curr_target]
                else:
                    ways = table[index-1][i]
                row.append(ways)
            table.append(copy.deepcopy(row))

        return table[-1][-1]
if __name__ == '__main__':
    soln = Solution()
    print(soln.combinationSum([1,2,5], 5))
    print(soln.combinationSum([2,3,6,7], 7))