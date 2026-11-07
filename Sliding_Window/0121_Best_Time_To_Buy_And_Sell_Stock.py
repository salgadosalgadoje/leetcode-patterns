"""
Problem: 121. Best Time to Buy and Sell Stock
Category: Sliding Window / Two Pointers
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0  # Puntero de compra (Buy)
        right = 1 # Puntero de venta (Sell)
        max_profit = 0

        while right < len(prices):
            # ¿Es una transacción rentable?
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                # Encontramos un precio más bajo, actualizamos nuestro día de compra
                # Movemos 'left' directamente a la posición de 'right'
                left = right
            
            # Siempre avanzamos el día de venta para seguir explorando
            right += 1
            
        return max_profit

if __name__ == "__main__":
    solution = Solution()
    
    # Casos de prueba de NeetCode
    assert solution.maxProfit([10, 1, 5, 6, 7, 1]) == 6, "Test 1 Falló"
    assert solution.maxProfit([10, 8, 7, 5, 2]) == 0, "Test 2 Falló"
    
    # Caso de prueba oficial de LeetCode (tradicional)
    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5, "Test 3 Falló"
    
    print("¡Todos los tests pasaron exitosamente!")