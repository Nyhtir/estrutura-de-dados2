from graphviz import Digraph
import random

class AVLNode:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, valor):
        def _insert(node, valor):
            if not node:
                return AVLNode(valor)
            if valor < node.valor:
                node.left = _insert(node.left, valor)
            elif valor > node.valor:
                node.right = _insert(node.right, valor)
            else:
                return node

            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
            balance = self.get_balance(node)

           
            if balance > 1 and valor < node.left.valor:
                return self.rotate_right(node)
        
            if balance < -1 and valor > node.right.valor:
                return self.rotate_left(node)
         
            if balance > 1 and valor > node.left.valor:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)
         
            if balance < -1 and valor < node.right.valor:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)
            return node

        self.root = _insert(self.root, valor)

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def rotate_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def visualize(self):
        dot = Digraph()
        def _add_edges(node):
            if node:
                dot.node(str(node.valor), f"{node.valor}\n(h={node.height})")
                if node.left:
                    dot.edge(str(node.valor), str(node.left.valor))
                    _add_edges(node.left)
                if node.right:
                    dot.edge(str(node.valor), str(node.right.valor))
                    _add_edges(node.right)
        _add_edges(self.root)
        return dot

    def inorder(self):
        def _inorder(node):
            if not node:
                return []
            return _inorder(node.left) + [node.valor] + _inorder(node.right)
        return _inorder(self.root)

    def height(self):
        return self.get_height(self.root) - 1


print("Rotações Simples:")
avl1 = AVLTree()
for v in [10, 20, 30]:
    avl1.insert(v)
    dot_avl = avl1.visualize()
    dot_avl.render(f'avl_simple_{v}', format='png', view=True)
    print(f"Inserido {v}: Inorder ->", avl1.inorder())


print("\nRotação Dupla:")
avl2 = AVLTree()
for v in [10, 30, 20]:
    avl2.insert(v)
    dot_avl2 = avl2.visualize()
    dot_avl2.render(f'avl_double_{v}', format='png', view=True)
    print(f"Inserido {v}: Inorder ->", avl2.inorder())


print("\nÁrvore AVL com valores randômicos:")
avl_rand = AVLTree()
rand_vals = random.sample(range(1, 101), 20)
for v in rand_vals:
    avl_rand.insert(v)
dot_avl_rand = avl_rand.visualize()
dot_avl_rand.render('avl_random', format='png', view=True)
print("Valores inseridos:", rand_vals)
print("Inorder:", avl_rand.inorder())
print("Altura da árvore AVL randômica:", avl_rand.height())
