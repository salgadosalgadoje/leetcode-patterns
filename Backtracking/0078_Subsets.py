"""
Problem: 78. Subsets
Category: Backtracking
Difficulty: Medium
Subsets
Medium
Topics
Company Tags
Hints
Given an array nums of unique integers, return all possible subsets of nums.

The solution set must not contain duplicate subsets. You may return the solution in any order.

Example 1:

Input: nums = [1,2,3]

Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [7]

Output: [[],[7]]
Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10

Time Complexity: O(n * 2^n) - Hay 2^n subconjuntos y copiar cada uno toma hasta O(n)
Space Complexity: O(n) - Profundidad máxima de la pila de recursión (sin contar el espacio de salida)
"""
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(index: int):
            # Caso base: hemos tomado una decisión para todos los elementos de nums
            if index >= len(nums):
                # Guardamos una copia del subconjunto actual (importante usar .copy())
                result.append(subset.copy())
                return

            # Decisión 1: INCLUIR nums[index] en el subconjunto actual
            subset.append(nums[index])
            backtrack(index + 1)

            # Paso de Backtracking: deshacemos la decisión anterior limpiando el último elemento
            subset.pop()

            # Decisión 2: NO INCLUIR nums[index] en el subconjunto actual
            backtrack(index + 1)

        backtrack(0)
        return result

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1: [1, 2, 3] -> 8 subconjuntos
    res1 = solution.subsets([1, 2, 3])
    expected1 = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert sorted(res1) == sorted(expected1), "Test 1 Falló"
    
    # Example 2: [7] -> 2 subconjuntos
    res2 = solution.subsets([7])
    expected2 = [[], [7]]
    assert sorted(res2) == sorted(expected2), "Test 2 Falló"
    
    print("¡Todos los tests pasaron exitosamente!")