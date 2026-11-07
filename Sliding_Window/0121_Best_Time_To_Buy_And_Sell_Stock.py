"""
Best Time to Buy and Sell Stock
Easy
Topics
Company Tags
Hints
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:

Input: prices = [10,1,5,6,7,1]

Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:

Input: prices = [10,8,7,5,2]

Output: 0
Explanation: No profitable transactions can be made, thus the max profit is 0.

Constraints:

1 <= prices.length <= 100
0 <= prices[i] <= 100
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