from typing import *

class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_num = str(x)
        length = len(str_num)
        output = True
        for index in range(len(str_num)):
            if(2*index <= length):
                if(str_num[index] != str_num[length-index-1]):
                    output = False
        return output

if(__name__ == '__main__'):
    soln = Solution()
    print(soln.isPalindrome(12345))
    print(soln.isPalindrome(-1221))
    print(soln.isPalindrome(1221))
    print(soln.isPalindrome(121))
    print(soln.isPalindrome(0))