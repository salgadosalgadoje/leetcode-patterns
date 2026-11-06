"""
Contains Duplicate
Easy
Topics
Company Tags
Hints
Given an integer array nums, 
return true if any value appears more than once in the array, 
otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9

"""
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
            
        return False

if __name__ == "__main__":
    solution = Solution()
    
    # Pruebas con el nuevo nombre de la función
    assert solution.hasDuplicate([1, 2, 3, 3]) == True, "Test 1 Falló"
    assert solution.hasDuplicate([1, 2, 3, 4]) == False, "Test 2 Falló"
    
    print("¡Todos los tests pasaron exitosamente!")