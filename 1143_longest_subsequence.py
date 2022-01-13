from typing import *

class Solution:
    def longestCommonSubsequence_1(self, text1: str, text2: str) -> int:
        if(len(text1) == 0 or len(text2) == 0):
            return 0
        output = 0
        for i in range(len(text2)):
            char = text2[i]
            indexIn1 = -1
            try:
                indexIn1 = text1.index(char)
            except:
                pass
            if(indexIn1 == -1):
                continue
            
            output = max(output, 1 + self.longestCommonSubsequence(text1[indexIn1+1:], text2[i+1:]))
        return output
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        shorter = None
        longer = None
        len1 = len(text1)
        len2 = len(text2)
        if(len1 == 0 or len2 == 0):
            return 0
        if(text1 == text2):
            return len1

        if(len1 >= len2):
            longer = text1[::-1]
            shorter = text2[::-1]
        else:
            longer = text2[::-1]
            shorter = text1[::-1]
        
        table = [[0]*(len(longer)+1)]
        
        for i in range(len(shorter)):
            row = [0]
            for j in range(len(longer)):
                length = None
                if(shorter[i] == longer[j]):
                    length = 1 + table[-1][j]
                else:
                    length = max(row[-1], table[-1][j+1])
                row.append(length)
            table.append(row)
        
        # for row in table:
        #     print(row)
        return table[-1][-1]

if __name__ == '__main__':
    soln = Solution()
    print(soln.longestCommonSubsequence("abcde", "axe"))
    print(soln.longestCommonSubsequence("abcde", "ace"))
    print(soln.longestCommonSubsequence("", ""))
    print(soln.longestCommonSubsequence(" ", "abc"))
    # print("aceee".index('d'))