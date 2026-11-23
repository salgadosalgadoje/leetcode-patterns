"""
Problem: 208. Implement Trie (Prefix Tree)
Category: Tries
Difficulty: Medium
A prefix tree (also known as a trie) is a tree data structure used to efficiently store and retrieve keys in a set of strings. Some applications of this data structure include auto-complete and spell checker systems.

Implement the PrefixTree class:

PrefixTree() Initializes the prefix tree object.
void insert(String word) Inserts the string word into the prefix tree.
boolean search(String word) Returns true if the string word is in the prefix tree (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
Example 1:

Input:
["Trie", "insert", "dog", "search", "dog", "search", "do", "startsWith", "do", "insert", "do", "search", "do"]

Output:
[null, null, true, false, true, null, true]

Explanation:
PrefixTree prefixTree = new PrefixTree();
prefixTree.insert("dog");
prefixTree.search("dog");    // return true
prefixTree.search("do");     // return false
prefixTree.startsWith("do"); // return true
prefixTree.insert("do");
prefixTree.search("do");     // return true
Constraints:

1 <= word.length, prefix.length <= 1000
word and prefix are made up of lowercase English letters.

Time Complexity: O(L) por operación (insert, search, startsWith), donde L es la longitud de la palabra/prefijo.
Space Complexity: O(N * L) en el peor caso, donde N es el número de palabras insertadas y L su longitud promedio.
"""

class TrieNode:
    def __init__(self):
        # Diccionario para almacenar los nodos hijos: {'a': TrieNode(), ...}
        self.children = {}
        # Marca si este nodo representa el final de una palabra completa
        self.end_of_word = False

class PrefixTree:
    def __init__(self):
        # El árbol siempre inicia con un nodo raíz vacío
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            # Si el carácter no existe como hijo del nodo actual, lo creamos
            if char not in current.children:
                current.children[char] = TrieNode()
            # Avanzamos al nodo hijo correspondiente
            current = current.children[char]
        
        # Al terminar el recorrido de la palabra, marcamos el nodo final
        current.end_of_word = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        
        # Para que sea una palabra válida, debe estar marcada como final de palabra
        # (Ej: si insertamos "dog", buscar "do" retornará False)
        return current.end_of_word

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
            
        # Si logramos recorrer todo el prefijo sin romper la cadena, existe al menos una palabra
        return True

if __name__ == "__main__":
    prefixTree = PrefixTree()
    
    # Secuencia de pruebas del Example 1
    prefixTree.insert("dog")
    assert prefixTree.search("dog") == True, "Test 1 Falló: 'dog' debería existir"
    assert prefixTree.search("do") == False, "Test 2 Falló: 'do' aún no ha sido insertada"
    assert prefixTree.startsWith("do") == True, "Test 3 Falló: 'dog' empieza con 'do'"
    
    prefixTree.insert("do")
    assert prefixTree.search("do") == True, "Test 4 Falló: 'do' ahora sí debería existir"
    assert prefixTree.startsWith("cat") == False, "Test 5 Falló: 'cat' no existe"
    
    print("¡Todos los tests pasaron exitosamente!")