from typing import *
import copy

class Solution:
    # submitted
    def lengthOfLongestSubstring2(self, s: str) -> int:
        output = ""
        longest = ""
        for char in s:
            if(char in output):
                if(len(output) > len(longest)):
                    longest = output
                
                index = output.index(char)
                output = output[index+1:]
            output += char
        if(len(output) > len(longest)):
            longest = output

        return len(longest)

    def lengthOfLongestSubstring(self, s: str) -> int:
        str_list = list(s)
        output = []
        longest = []
        for char in str_list:
            if(char in output):
                if(len(output) > len(longest)):
                    longest = copy.deepcopy(output)
                
                index = output.index(char)
                output = output[index:]
                output.pop(0)
            output.append(char)
        if(len(output) > len(longest)):
            longest = copy.deepcopy(output)

        output_str = ""
        output_str = output_str.join(longest)
        return len(output_str)

if __name__ == '__main__':
    soln = Solution()
    print(soln.lengthOfLongestSubstring2('abcabcbb'))
    print(soln.lengthOfLongestSubstring2('bbbbb'))
    print(soln.lengthOfLongestSubstring2('pwwkew'))
    print(soln.lengthOfLongestSubstring2(''))
    print(soln.lengthOfLongestSubstring2(' '))
    print(soln.lengthOfLongestSubstring2('a'))
    print(soln.lengthOfLongestSubstring2('dvdf'))