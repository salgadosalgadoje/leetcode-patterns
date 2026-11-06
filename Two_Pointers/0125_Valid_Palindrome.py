"""
Valid Palindrome
Easy
Topics
Company Tags
Hints
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:

1 <= s.length <= 1000
s is made up of only printable ASCII characters.

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