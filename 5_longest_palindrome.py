from typing import *

class Solution:
    def isPalindrome(self, s):
        # print('Checking string ', s)
        if(len(s) == 1):
            return True
        # for i in range(int(len(s)/2)):
        #     if(s[i] != s[len(s)-i-1]):
        #         return False
        reversed = s[::-1]
        if(reversed == s):
            return True
        else:
            return False

    def longestPalindrome(self, s: str) -> str:
        if(self.isPalindrome(s)):
            return s
        else:
            output_r = self.longestPalindrome(s[1:])
            output_l = self.longestPalindrome(s[:len(s)-1])
            if(len(output_r) > len(output_l)):
                return output_r
            else:
                return output_l
    
    def longestPalindrome_dp(self, s:str) -> str:
        if(len(s) <= 1):
            return s
        table = []
        
        for i in range(len(s)):
            table.append([s[0]])
        
        table[0].extend(list(s[1:]))
        
        for length in range(1,len(s)):
            for index in range(1,len(s)):
                if(index < length):
                    table[length].append(table[length-1][index])
                elif(self.isPalindrome(s[index-length:index+1])):
                    table[length].append(s[index-length:index+1])
                else:
                    current = ''
                    if(len(table[length-1][index]) > len(table[length][index-1])):
                        current = table[length-1][index]
                    else:
                        current = table[length][index-1]
                    table[length].append(current)
                # print(table)
        # for row in table:
        #     print(row)

        return table[-1][-1]
    
    # submitted
    def longestPalindrome_dp2(self, s:str) -> str:
        if(len(s) <= 1):
            return s
        
        if(s == s[::-1]):
            return s

        output = s[0]
        table = []
        for i in range(len(s)):
            lst = [0] * len(s)
            lst[i] = 1
            table.append(lst)

        for i in range(len(s)-1):
            if(s[i] == s[i+1]):
                table[i][i+1] = 1
                if(2 > len(output)):
                    output = s[i:i+2]
        for length in range(2, len(s)):
            for startIndex in range(len(s)):
                if(startIndex + length >= len(s)):
                    continue
                if(s[startIndex] == s[startIndex + length] and table[startIndex+1][startIndex+length-1]):
                    # print(s[startIndex: startIndex + length + 1], s[startIndex] == s[startIndex + length], table[startIndex+1][startIndex+length-1])
                    table[startIndex][startIndex+length] = 1

                    if(len(s[startIndex: startIndex+length+1]) > len(output)):
                        output = s[startIndex: startIndex+length+1]
        # for row in table:
        #     print(row)
        return output
        

if __name__ == '__main__':
    soln = Solution()
    print(soln.longestPalindrome_dp2('cbbbd'))
    print(soln.longestPalindrome_dp2('abcdefghijklmnopqrstuvwxyz'))
    print(soln.longestPalindrome_dp2('a'))
    print(soln.longestPalindrome_dp2("lphbehiapswjudnbcossedgioawodnwdruaaxhbkwrxyzaxygmnjgwysafuqbmtzwdkihbwkrjefrsgjbrycembzzlwhxneiijgzidhngbmxwkhphoctpilgooitqbpjxhwrekiqupmlcvawaiposqttsdgzcsjqrmlgyvkkipfigttahljdhtksrozehkzgshekeaxezrswvtinyouomqybqsrtegwwqhqivgnyehpzrhgzckpnnpvajqevbzeksvbezoqygjtdouecnhpjibmsgmcqcgxwzlzztdneahixxhwwuehfsiqghgeunpxgvavqbqrelnvhnnyqnjqfysfltclzeoaletjfzskzvcdwhlbmwbdkxnyqappjzwlowslwcbbmcxoiqkjaqqwvkybimebapkorhfdzntodhpbhgmsspgkbetmgkqlolsltpulgsmyapgjeswazvhxedqsypejwuzlvegtusjcsoenrcmypexkjxyduohlvkhwbrtzjnarusbouwamazzejhnetfqbidalfomecehfmzqkhndpkxinzkpxvhwargbwvaeqbzdhxzmmeeozxxtzpylohvdwoqocvutcelgdsnmubyeeeufdaoznxpvdiwnkjliqtgcmvhilndcdelpnilszzerdcuokyhcxjuedjielvngarsgxkemvhlzuprywlypxeezaxoqfges"))
    print(soln.longestPalindrome_dp2('000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'))