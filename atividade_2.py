import random
from graphviz import Digraph

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, valor):
        def _insert(node, valor):
            if node is None:
                return Node(valor)
            if valor < node.valor:
                node.left = _insert(node.left, valor)
            elif valor > node.valor:
                node.right = _insert(node.right, valor)
            return node
        self.root = _insert(self.root, valor)

    def search(self, valor):
        def _search(node, valor):
            if node is None:
                return False
            if node.valor == valor:
                return True
            elif valor < node.valor:
                return _search(node.left, valor)
            else:
                return _search(node.right, valor)
        return _search(self.root, valor)

    def delete(self, valor):
        def _min_value_node(node):
            current = node
            while current.left:
                current = current.left
            return current

        def _delete(node, valor):
            if node is None:
                return node
            if valor < node.valor:
                node.left = _delete(node.left, valor)
            elif valor > node.valor:
                node.right = _delete(node.right, valor)
            else:
            
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
        
                temp = _min_value_node(node.right)
                node.valor = temp.valor
                node.right = _delete(node.right, temp.valor)
            return node
        self.root = _delete(self.root, valor)

    def height(self):
        def _height(node):
            if node is None:
                return -1
            return 1 + max(_height(node.left), _height(node.right))
        return _height(self.root)

    def depth(self, valor):
        def _depth(node, valor, d):
            if node is None:
                return -1
            if node.valor == valor:
                return d
            elif valor < node.valor:
                return _depth(node.left, valor, d+1)
            else:
                return _depth(node.right, valor, d+1)
        return _depth(self.root, valor, 0)

    def visualize(self):
        dot = Digraph()
        def _add_edges(node):
            if node:
                dot.node(str(node.valor), str(node.valor))
                if node.left:
                    dot.edge(str(node.valor), str(node.left.valor))
                    _add_edges(node.left)
                if node.right:
                    dot.edge(str(node.valor), str(node.right.valor))
                    _add_edges(node.right)
        _add_edges(self.root)
        return dot

valores = [55, 30, 80, 20, 45, 70, 90]
bst = BinarySearchTree()
for v in valores:
    bst.insert(v)
dot_bst = bst.visualize()
dot_bst.render('bst_fixed', format='png', view=True)


print("Busca pelo valor 45:", bst.search(45))
bst.delete(30)
print("Após remover 30, busca por 30:", bst.search(30))
bst.insert(60)
print("Após inserir 60, busca por 60:", bst.search(60))
print("Altura da árvore:", bst.height())
print("Profundidade do nó 45:", bst.depth(45))


random_numbers = random.sample(range(1, 201), 15)
bst_random = BinarySearchTree()
for num in random_numbers:
    bst_random.insert(num)
dot_bst_random = bst_random.visualize()
dot_bst_random.render('bst_random', format='png', view=True)
print("Números aleatórios:", random_numbers)
print("Altura da árvore aleatória:", bst_random.height())
