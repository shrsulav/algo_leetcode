from typing import *

class Solution:        
    def canBeValid(self, s: str, locked: str) -> bool:
        # if(len(s) != len(locked)):
        #     return False
        
        if(len(s) % 2 != 0):
            return False
        
        freeIndex = 0
        locked_open = 0
        locked_close = 0
        for i in range(len(s)):
            if(locked[i] == '0'):
                freeIndex += 1
            elif(s[i] == '('):
                locked_open += 1
            else:
                locked_close += 1
                # print(locked[:i+1])
                # print(s[:i+1])
                if(not (locked_open + freeIndex >= locked_close)):
                    return False
        freeIndex = 0
        locked_open = 0
        locked_close = 0
        for i in range(len(s)-1, -1, -1):
            if(locked[i] == '0'):
                freeIndex += 1
            elif(s[i] == '('):
                locked_open += 1
                # print(locked[i:])
                # print(s[i:])
                if(not (locked_close + freeIndex >= locked_open)):
                    return False
            else:
                locked_close += 1
                
        return True

if __name__ == '__main__':
    soln = Solution()
    print(soln.canBeValid('((()', '1110'))
    print(soln.canBeValid('()))', '0111'))
    print(soln.canBeValid("))()))", "010100"))
    print(soln.canBeValid(")", "0"))
    print(soln.canBeValid('((((((((', '11110000'))
    print(soln.canBeValid('))))((((', '11110000'))
    print(soln.canBeValid('', ''))
    print(soln.canBeValid("())(()(()(())()())(())((())(()())((())))))(((((((())(()))))(", "100011110110011011010111100111011101111110000101001101001111"))
