from typing import *

class Solution:
    def isValid(self, s: str) -> bool:
        table = {'(': ')', '[':']', '{': '}'}
        if(len(s) % 2 != 0):
            return False
        stack = []

        for char in s:
            if char in table:
                stack.append(char)
            else:
                if(len(stack) == 0):
                    return False
                if(table[stack.pop()] != char):
                    return False
        if(len(stack) != 0):
            return False
        else:
            return True

if __name__ == '__main__':
    soln = Solution()
    print(soln.isValid('()[]{}'))
    print(soln.isValid('()'))
    print(soln.isValid(''))
    print(soln.isValid('('))
    print(soln.isValid('(}'))
    print(soln.isValid("{[]}"))
