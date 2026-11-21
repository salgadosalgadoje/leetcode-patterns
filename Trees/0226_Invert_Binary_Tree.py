"""
Problem: 226. Invert Binary Tree
Category: Trees
Difficulty: Easy
Hints
You are given the root of a binary tree root. Invert the binary tree and return its root.

Example 1:



Input: root = [1,2,3,4,5,6,7]

Output: [1,3,2,7,6,5,4]
Example 2:



Input: root = [3,2,1]

Output: [3,1,2]
Example 3:

Input: root = []

Output: []
Constraints:

0 <= The number of nodes in the tree <= 100.
-100 <= Node.val <= 100
Time Complexity: O(n)
Space Complexity: O(h) - donde h es la altura del árbol (O(n) en el peor caso, O(log n) si está balanceado)
"""
from typing import Optional, List
from collections import deque

# Definición para un nodo de un árbol binario.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Caso base: si el nodo es nulo, no hay nada que invertir
        if not root:
            return None
        
        # Intercambiamos los hijos izquierdo y derecho en un solo paso (Pythonic swap)
        root.left, root.right = root.right, root.left
        
        # Invertimos recursivamente los subárboles izquierdo y derecho
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

# Funciones auxiliares para convertir listas (formato LeetCode) a Árboles y viceversa
def list_to_tree(elements: List[Optional[int]]) -> Optional[TreeNode]:
    if not elements or elements[0] is None:
        return None
    root = TreeNode(elements[0])
    queue = deque([root])
    i = 1
    while queue and i < len(elements):
        current = queue.popleft()
        if i < len(elements) and elements[i] is not None:
            current.left = TreeNode(elements[i])
            queue.append(current.left)
        i += 1
        if i < len(elements) and elements[i] is not None:
            current.right = TreeNode(elements[i])
            queue.append(current.right)
        i += 1
    return root

def tree_to_list(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        current = queue.popleft()
        if current:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
    return result

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1: [1, 2, 3, 4, 5, 6, 7] -> [1, 3, 2, 7, 6, 5, 4]
    tree1 = list_to_tree([1, 2, 3, 4, 5, 6, 7])
    inverted1 = solution.invertTree(tree1)
    assert tree_to_list(inverted1) == [1, 3, 2, 7, 6, 5, 4], "Test 1 Falló"
    
    # Example 2: [3, 2, 1] -> [3, 1, 2]
    tree2 = list_to_tree([3, 2, 1])
    inverted2 = solution.invertTree(tree2)
    assert tree_to_list(inverted2) == [3, 1, 2], "Test 2 Falló"
    
    # Example 3: [] -> []
    tree3 = list_to_tree([])
    inverted3 = solution.invertTree(tree3)
    assert tree_to_list(inverted3) == [], "Test 3 Falló"
    
    print("¡Todos los tests pasaron exitosamente!")