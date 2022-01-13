from typing import *

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        row = [1]
        row.extend([0]*amount)
        table = [row]
        print(table)
        for coin_index in range(len(coins)-1, -1, -1):
            row = [1]
            for i in range(1, amount+1):
                num_ways = 0
                if(coins[coin_index]<=i):
                    num_ways = row[i-coins[coin_index]] + table[-1][i]
                row.append(num_ways)
            table.append(row)
        for row in table:
            print(row)
        return table[-1][-1]

if __name__ == '__main__':
    soln = Solution()
    # print(soln.change(5, [1,2,5]))
    # print(soln.change(5, [6,7]))
    # print(soln.change(5, []))
    print(soln.change(100, [99, 1]))