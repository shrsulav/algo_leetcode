from typing import *

class Solution:
    def gen(self, string, n_open, n_close, output):
        if(n_open == 0 and n_close == 0):
            # print(string)
            output.append(string)
        elif(n_open == 0):
            self.gen(string+')', n_open, n_close-1, output)
        elif(n_open < n_close):
            self.gen(string+'(', n_open-1,n_close, output)
            self.gen(string+')', n_open, n_close-1, output)
        elif(n_open == n_close):
            self.gen(string+'(', n_open-1,n_close, output)
            
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        self.gen('(', n-1, n, output)
        return output
if(__name__ == '__main__'):
    soln = Solution()
    output = soln.generateParenthesis(3)
    print(output)