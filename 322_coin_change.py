from typing import *

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        changeTable = [0]
        for i in range(1, amount+1):
            minCoins = float('inf')
            for coin in coins:
                if(coin <= i):
                    minCoins = min(minCoins, 1+changeTable[i-coin])
            changeTable.append(minCoins)
        
        output = changeTable[amount]
        if(output == float('inf')):
            output = -1
        return output

if __name__ == '__main__':
    soln = Solution()
    print(soln.coinChange([1,2,5], 11))
    print(soln.coinChange([], 11))
    print(soln.coinChange([], 0))
    print(soln.coinChange([5], 11))