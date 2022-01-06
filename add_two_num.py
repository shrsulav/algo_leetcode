from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def print(self, l: Optional[ListNode]) -> None:
        current = l
        while(current != None):
            print(current.val)
            current = current.next
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_list = None
        current_l1 = l1
        current_l2 = l2
        current_sum = sum_list
        carry = False
        while(current_l2 != None or current_l1 != None):
            if(sum_list == None):
                sum_list = ListNode()
                current_sum = sum_list
            elif(not carry):
                current_sum.next = ListNode()
                current_sum = current_sum.next

            t_sum = current_sum.val
            last_digit = 0
            carry = False
            if(current_l2 != None):
                t_sum += current_l2.val
                current_l2 = current_l2.next
            
            if(current_l1 != None):
                t_sum += current_l1.val
                current_l1 = current_l1.next
            
            if(carry):
                t_sum += 1

            if(t_sum > 9):
                last_digit = t_sum % 10
                carry = True
            else:
                last_digit = t_sum

            current_sum.val = last_digit
            if(carry):
                current_sum.next = ListNode(1)
                current_sum = current_sum.next
            
        return sum_list


if(__name__ == '__main__'):
    l1 = ListNode(1)
    l1.next = ListNode(5)
    l2 = ListNode(2)
    l2.next = ListNode(6)
    soln = Solution()
    output = soln.addTwoNumbers(l1, l2)
    soln.print(output)