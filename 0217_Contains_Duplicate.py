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