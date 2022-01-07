from typing import *

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        changePosition = None
        swapPosition = None
        for index in range(len(nums)-1, 0, -1):
            if(nums[index-1] < nums[index]):
                changePosition = index-1
                for index in range(len(nums)-1, changePosition, -1):
                    if nums[index] > nums[changePosition]:
                        swapPosition = index
                        break
                nums[changePosition], nums[swapPosition] = nums[swapPosition], nums[changePosition]
                self.quickSort(nums, changePosition+1, len(nums)-1)
                break
        if(changePosition == None):
            self.quickSort(nums, 0, len(nums)-1)
        print(nums)

    # sorting algorithm taken from geeks for geeks
    # https://www.geeksforgeeks.org/python-program-for-quicksort/
    def partition(self, arr, low, high):
        i = (low-1)         # index of smaller element
        pivot = arr[high]     # pivot
    
        for j in range(low, high):
        
            # If current element is smaller than or
            # equal to pivot
            if arr[j] <= pivot:
            
                # increment index of smaller element
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
    
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)
    
    def quickSort(self, arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:
        
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self.partition(arr, low, high)
    
            # Separately sort elements before
            # partition and after partition
            self.quickSort(arr, low, pi-1)
            self.quickSort(arr, pi+1, high)

if __name__ == '__main__':
    soln = Solution()
    soln.nextPermutation([1,2,3])
    soln.nextPermutation([1,4,3,2])
    soln.nextPermutation([1,1,5])
    soln.nextPermutation([1,5,1])
    soln.nextPermutation([3,2,1])
    soln.nextPermutation([0])
    soln.nextPermutation([])