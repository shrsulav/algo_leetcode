from typing import *
import copy
import math

class Solution:
    def __init__(self) -> None:
        self.counter = 0
    def giveSolution(self, nums, current, n, k):
        if(len(current) == n):
            self.counter += 1
            str1 = ""
            print(self.counter , ':',str1.join(current))
            # return str1.join(current)

        t_nums = copy.deepcopy(nums)
        for index, num in enumerate(nums):
            current.append(num)
            t_nums.pop(index)
            tmp = self.giveSolution(t_nums, current, n, k)
            # if(self.counter == k):
            #     return tmp
            t_nums.insert(index, num)
            current.pop()
    
    def getPermutation(self, n: int, k: int) -> str:
        nums = []
        self.counter = 0
        for i in range(n):
            nums.append(str(i+1))
        return self.giveSolution(nums, [], n, k)

    # submitted
    def getPermutation2(self,n,k):
        nums = []
        output = ""
        for i in range(n):
            nums.append(str(i+1))
        
        while(len(nums)):
            counter = 0
            index = 0
            while(counter < k):
                t_counter = math.factorial(n-1)
                if(t_counter + counter >= k):
                    break
                index += 1
                counter += t_counter
            # print(nums[index])
            output += nums[index]
            # print(output)
            nums.pop(index)
            n = n - 1
            k = k - counter
        return output
if __name__ == '__main__':
    soln = Solution()
    print(soln.getPermutation2(3,3))
    # print(soln.getPermutation2(4,9))
    print(soln.getPermutation2(4,9))
    print(soln.getPermutation2(3,1))
    print(soln.getPermutation2(9,199269))
