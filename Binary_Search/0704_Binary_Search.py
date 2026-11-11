"""
Binary Search
Easy
Topics
Company Tags
Hints
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in 
O(logn)
O(logn) time.

Example 1:

Input: nums = [-1,0,2,4,6,8], target = 4

Output: 3
Example 2:

Input: nums = [-1,0,2,4,6,8], target = 3

Output: -1
Constraints:

1 <= nums.length <= 10000.
-10000 < nums[i], target < 10000
All the integers in nums are unique.

"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            # Calculamos el punto medio de forma segura
            mid = left + (right - left) // 2

            # Caso 1: Encontramos el target exactamente en el medio
            if nums[mid] == target:
                return mid
            
            # Caso 2: El target es mayor, descartamos toda la mitad izquierda
            elif nums[mid] < target:
                left = mid + 1
            
            # Caso 3: El target es menor, descartamos toda la mitad derecha
            else:
                right = mid - 1

        # Si el ciclo termina y no lo encontramos, retornamos -1
        return -1

if __name__ == "__main__":
    solution = Solution()
    
    # Casos de prueba de la descripción
    assert solution.search([-1, 0, 2, 4, 6, 8], 4) == 3, "Test 1 Falló"
    assert solution.search([-1, 0, 2, 4, 6, 8], 3) == -1, "Test 2 Falló"
    
    # Casos límite adicionales
    assert solution.search([5], 5) == 0, "Test 3 Falló"
    assert solution.search([1, 3], 0) == -1, "Test 4 Falló"
    
    print("¡Todos los tests pasaron exitosamente!")