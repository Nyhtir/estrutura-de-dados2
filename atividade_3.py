from graphviz import Digraph
import random

class BinaryTreeNode:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, valor):
        if self.root is None:
            self.root = BinaryTreeNode(valor)
        else:
            queue = [self.root]
            while queue:
                node = queue.pop(0)
                if not node.left:
                    node.left = BinaryTreeNode(valor)
                    break
                else:
                    queue.append(node.left)
                if not node.right:
                    node.right = BinaryTreeNode(valor)
                    break
                else:
                    queue.append(node.right)

    def inorder(self):
        def _inorder(node):
            if not node:
                return []
            return _inorder(node.left) + [node.valor] + _inorder(node.right)
        return _inorder(self.root)

    def preorder(self):
        def _preorder(node):
            if not node:
                return []
            return [node.valor] + _preorder(node.left) + _preorder(node.right)
        return _preorder(self.root)

    def postorder(self):
        def _postorder(node):
            if not node:
                return []
            return _postorder(node.left) + _postorder(node.right) + [node.valor]
        return _postorder(self.root)

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


valores_fixos = [55, 30, 80, 20, 45, 70, 90]
bt_fixed = BinaryTree()
for v in valores_fixos:
    bt_fixed.insert(v)
dot_fixed = bt_fixed.visualize()
dot_fixed.render('binary_tree_fixed', format='png', view=True)
print("Árvore Binária com Valores Fixos:")
print("Inorder:", bt_fixed.inorder())
print("Preorder:", bt_fixed.preorder())
print("Postorder:", bt_fixed.postorder())


random_vals = random.sample(range(1, 101), 10)
bt_random = BinaryTree()
for v in random_vals:
    bt_random.insert(v)
dot_random = bt_random.visualize()
dot_random.render('binary_tree_random', format='png', view=True)
print("\nÁrvore Binária com Valores Randômicos:", random_vals)
print("Inorder:", bt_random.inorder())
print("Preorder:", bt_random.preorder())
print("Postorder:", bt_random.postorder())
