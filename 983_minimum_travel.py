from typing import *

class Solution:
    def __init__(self):
        self.pass_table = [1,7,30]
    def mincostTickets_1(self, days: List[int], costs: List[int]) -> int:
        if not days:
            return 0
        min_cost = float('inf')
        last_day = days[0]
        for index in range(len(costs)):
            current_cost = costs[index]
            future_days = []

            for day in days:
                if(day >= days[0]+self.pass_table[index]):
                    future_days.append(day)
            current_cost += self.mincostTickets_1(future_days, costs)

            min_cost = min(current_cost, min_cost)
        return min_cost
        
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        table = {}
        for day_index in range(len(days)-1, -1, -1):
            current_min = float('inf')
            for index in range(len(costs)):
                current_cost = costs[index]
                till_day = days[day_index] + self.pass_table[index]
                current_index  = day_index
                while current_index in range(len(days)):
                    if(days[current_index] < till_day):
                        current_index += 1
                    else:
                        break
                if(current_index in table):
                    current_cost += table[current_index]
                current_min = min(current_min, current_cost)
            table[day_index] = current_min    
        return table[0]
if __name__ == '__main__':
    soln = Solution()
    print(soln.mincostTickets([1,4,6,7,8,20], [2,7,15]))
    print(soln.mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]))
    print(soln.mincostTickets_2([1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,24,25,27,28,29,30,31,34,37,38,39,41,43,44,45,47,48,49,54,57,60,62,63,66,69,70,72,74,76,78,80,81,82,83,84,85,88,89,91,93,94,97,99],[9,38,134]))
    print(soln.mincostTickets([1,4,6,9,10,11,12,13,14,15,16,17,18,20,21,22,23,27,28], [3,13,45]))