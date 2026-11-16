"""
Problem: 20. Valid Parentheses
Category: Stack
Difficulty: Easy
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"

Output: true
Example 2:

Input: s = "([{}])"

Output: true
Example 3:

Input: s = "[(])"

Output: false
Explanation: The brackets are not closed in the correct order.

Constraints:

1 <= s.length <= 1000
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        # Pila para almacenar los paréntesis de apertura
        stack = []
        # Mapa de correspondencia: cierre -> apertura
        close_to_open = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s:
            # Si el carácter actual es de cierre
            if char in close_to_open:
                # Verificamos que la pila no esté vacía y que el tope coincida con su apertura
                if stack and stack[-1] == close_to_open[char]:
                    stack.pop()
                else:
                    return False
            else:
                # Si es de apertura, lo apilamos
                stack.append(char)

        # La cadena es válida solo si todos los paréntesis abiertos fueron cerrados (pila vacía)
        return len(stack) == 0

if __name__ == "__main__":
    solution = Solution()
    
    # Casos de prueba de la descripción
    assert solution.isValid("[]") == True, "Test 1 Falló"
    assert solution.isValid("([{}])") == True, "Test 2 Falló"
    assert solution.isValid("[(])") == False, "Test 3 Falló"
    
    # Casos límite importantes
    assert solution.isValid("]") == False, "Test 4 Falló (solo cierre)"
    assert solution.isValid("(((") == False, "Test 5 Falló (solo apertura)"
    
    print("¡Todos los tests pasaron exitosamente!")