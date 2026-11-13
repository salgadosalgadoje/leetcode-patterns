"""
Problem: 206. Reverse Linked List
Category: Linked List
Difficulty: Easy
Reverse Linked List
Easy
Topics
Company Tags
Hints
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
Example 1:

Input: head = [0,1,2,3]

Output: [3,2,1,0]

Example 2:

Input: head = []

Output: []

Constraints:

0 <= The length of the list <= 1000.
-1000 <= Node.val <= 1000 
"""
from typing import Optional, List

# Definición para un nodo de una lista enlazada simple.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        
        while current:
            # 1. Guardamos temporalmente el siguiente nodo para no perderlo
            next_node = current.next
            
            # 2. Invertimos el puntero: el nodo actual ahora apunta al anterior
            current.next = prev
            
            # 3. Avanzamos los punteros 'prev' y 'current' un paso hacia adelante
            prev = current
            current = next_node
            
        # Al finalizar, 'prev' queda posicionada en el nuevo inicio (la antigua cola)
        return prev

# Funciones auxiliares para transformar listas de Python a Linked Lists y viceversa (para testing)
def list_to_linkedlist(elements: List[int]) -> Optional[ListNode]:
    if not elements:
        return None
    head = ListNode(elements[0])
    current = head
    for val in elements[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linkedlist_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

if __name__ == "__main__":
    solution = Solution()
    
    # Test 1: [0, 1, 2, 3] -> [3, 2, 1, 0]
    head1 = list_to_linkedlist([0, 1, 2, 3])
    reversed1 = solution.reverseList(head1)
    assert linkedlist_to_list(reversed1) == [3, 2, 1, 0], "Test 1 Falló"
    
    # Test 2: Lista vacía [] -> []
    head2 = list_to_linkedlist([])
    reversed2 = solution.reverseList(head2)
    assert linkedlist_to_list(reversed2) == [], "Test 2 Falló"
    
    # Test 3: Lista de un solo elemento [5] -> [5]
    head3 = list_to_linkedlist([5])
    reversed3 = solution.reverseList(head3)
    assert linkedlist_to_list(reversed3) == [5], "Test 3 Falló"
    
    print("¡Todos los tests pasaron exitosamente!")