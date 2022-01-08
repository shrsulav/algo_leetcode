from typing import *
import copy
class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s) % 2 != 0):
            return False
        stack = []

        for char in s:
            if char=='(':
                stack.append(char)
            else:
                if(len(stack) == 0):
                    return False
                stack.pop()

        
        if(len(stack) != 0):
            return False
        else:
            return True
    def longestValidParentheses_1(self, s: str) -> int:
        if(self.isValid(s)):
            return len(s)
        else:
            if(len(s)>2):
                output1 = self.longestValidParentheses(s[:-1])
                output2 = self.longestValidParentheses(s[1:])
                if(output1 > output2):
                    return output1
                else:
                    return output2
            else:
                return 0
    
    def longestValidParentheses_2(self, s: str) -> int:
        if(len(s) <= 1):
            return 0
        if(len(s) == 2):
            if(s == '()'):
                return 2
            else:
                return 0
        
        table = []
        longest = 0
        for i in range(len(s)):
            tmp = [0]*len(s)
            table.append(tmp)
        valid = {}
        for index in range(0, len(s)-1):
            if(s[index:index+2] == '()'):
                table[index][index+1] = 1
                longest = 2
                valid[index] = index+1
        for length in range(3,len(s)+1):
            for index in range(0, len(s)):
                if(index+length > len(s)):
                   continue
                if(length % 2 != 0):
                    continue
                # print('Checking for ', index, index+length-1, s[index:index+length])
                if(s[index]=='(' and s[index+length-1] == ')' and table[index+1][index+length-2] != 0):
                    table[index][index+length-1] = 1
                    if(length > longest):
                        longest = length
                    
                elif(1 in table[index]):
                    if(table[table[index].index(1)+1][index+length-1] == 1):
                        table[index][index+length-1] = 1
                        if(length > longest):
                            longest = length
                        # print('start ', index, 'end', index+length-1, 'string', s[index:index+length])
        return longest
    def longestValidParentheses_3(self, s: str) -> int:
        if(len(s) <= 1):
            return 0
        stack = [-1]
        maxlength = 0
        breakIndex = -1
        for index in range(len(s)):
            if(s[index] == '('):
                stack.append(index)
            else:
                popped = stack.pop()
                if(popped == breakIndex):
                    stack.append(index)
                    breakIndex = index
                    continue
                length = index - stack[-1]
                if(length > maxlength):
                    maxlength = length
        return maxlength
    
    def longestValidParentheses(self, s: str) -> int:
        if(len(s) <= 1):
            return 0
        stack = [-1]
        maxlength = 0
        for index in range(len(s)):
            if(s[index] == '('):
                stack.append(index)
            else:
                stack.pop()
                if stack:
                    maxlength = max(maxlength, index-stack[-1])
                else:
                    stack.append(index)
        return maxlength
if __name__ == '__main__':
    soln = Solution()
    # 2
    print(soln.longestValidParentheses('(()'))
    # 4
    print(soln.longestValidParentheses('(())'))
    # 4
    print(soln.longestValidParentheses('()()'))
    # 6
    print(soln.longestValidParentheses('()()()'))
    # 10
    print(soln.longestValidParentheses('()(())(()))'))
    4
    print(soln.longestValidParentheses(")()())"))
    # 
    print(soln.longestValidParentheses("())()()(())((()(()()(((()))((((())((()(())()())(()((((()))()(()))(())()(())(()(((((())((((((()())())(()(()((())()))(()))))))()(()))((((())()()()))()()()(((()(()())(()()(()(()()(((()))))))()()))())())((()()))))))((()))(((()((())()(()()))((())))()()())))))))()))))(()))))()))()))()((())))((()))(()))))))(((()))))))))()(()()()(())((())()))()()(())))()()))(()())()))(((()())()))((())((((()))(()(()(()()()(((())()(((((()))((()(((((())(()()))((((((((()(()(()(()(())))(())(()())())(()((((()(())((()(())))(())))()(((((()(()()(())))))))())(())(())(()()(((())))((()))(((((()))))())))()((()))()))))())))))((())(((((()()))((((())))(((()(()(())())(((()(()(()()()())))())()))((()((())())()()()(((())(((((()((((((()((()())))((((())((()(((((((()(()((()()()(()(()())(()(()()((((())))()(((()())))(()()))()(()()()()(((((())(()))))((()))())))()((((((()))())))()(()))(())))((((()())(((((()()())(((((())(()())(()))))()(()()))()))))))())))(((())(()(()()))(()))()(((())))())((((()(((()))))))()(()(()))()()(()()))))))))((()))))))(())((()((()))()))((((((()())))))(()((())((((()))))(()(()()()()(()))()()(()(()))(()()(((((((()())(())(()())((())())()(()())((())()())())(()())))())))(())())())(())((()())(((()()))()))()()))()(()(())((((((((())))()((())((()((((((((((()))))(()(((((())(()(()())())))((())())))))()))(()((()()))((()((())()()()((()(())())((())())(()()(((())))))())()()(()))()())(()(()((())))((((()()(())))())(())(()(()(())())())(()()())()(())())))(()()(((())))((()()(((())()()(()())((((()()(()())(()((((()(()()(()(()(((()((()())(()()))(()((((()(((((()))))()()))(((()((((((()(()()()()())()))(()(())))))((()(((()())())))(((()()))(()(()(((((((()()))(()(())))())()(())())(())(()))(())(()))()()(()()())))))()))()((())(((()((((((((())()()))())))((()())("))