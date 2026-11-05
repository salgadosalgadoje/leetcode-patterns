"""
Problem: 125. Valid Palindrome
Category: Two Pointers
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # Avanzamos el puntero izquierdo si no es un carácter alfanumérico
            while left < right and not s[left].isalnum():
                left += 1
            
            # Retrocedemos el puntero derecho si no es un carácter alfanumérico
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Comparamos ambos caracteres convirtiéndolos a minúscula
            if s[left].lower() != s[right].lower():
                return False
            
            # Movemos ambos punteros para la siguiente iteración
            left += 1
            right -= 1
            
        return True

if __name__ == "__main__":
    solution = Solution()
    
    # Casos de prueba
    assert solution.isPalindrome("Was it a car or a cat I saw?") == True, "Test 1 Falló"
    assert solution.isPalindrome("tab a cat") == False, "Test 2 Falló"
    assert solution.isPalindrome(" ") == True, "Test 3 Falló"
    
    print("¡Todos los tests pasaron exitosamente!")