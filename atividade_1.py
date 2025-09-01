import random
from graphviz import Digraph

class ExprNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def parse_expression(tokens):
    """Parses a fully parenthesized infix expression into an expression tree."""
    stack = []
    for token in tokens:
        if token == ')':
            right = stack.pop()
            op = stack.pop()
            left = stack.pop()
            stack.pop() 
            stack.append(ExprNode(op, left, right))
        elif token in '+-*':
            stack.append(token)
        elif token == '(':
            stack.append(token)
        else:
            stack.append(ExprNode(token))
    return stack[0]

def visualize_expr_tree(node, dot=None):
    if dot is None:
        dot = Digraph()
    node_id = str(id(node))
    dot.node(node_id, str(node.value))
    if node.left:
        left_id = str(id(node.left))
        dot.edge(node_id, left_id)
        visualize_expr_tree(node.left, dot)
    if node.right:
        right_id = str(id(node.right))
        dot.edge(node_id, right_id)
        visualize_expr_tree(node.right, dot)
    return dot

def generate_random_expr():
    ops = ['+', '-', '*']
    nums = [str(random.randint(1, 20)) for _ in range(3)]
    op1, op2 = random.sample(ops, 2)
   
    if random.choice([True, False]):
        expr = f"( ( {nums[0]} {op1} {nums[1]} ) {op2} {nums[2]} )"
    else:
        expr = f"( {nums[0]} {op1} ( {nums[1]} {op2} {nums[2]} ) )"
    return expr

expr = '( ( 7 + 3 ) * ( 5 - 2 ) )'
tokens = expr.replace('(', ' ( ').replace(')', ' ) ').split()
root = parse_expression(tokens)
dot = visualize_expr_tree(root)
dot.render('expr_tree_fixed', format='png', view=True)


expr_rand = generate_random_expr()
tokens_rand = expr_rand.replace('(', ' ( ').replace(')', ' ) ').split()
root_rand = parse_expression(tokens_rand)
dot_rand = visualize_expr_tree(root_rand)
dot_rand.render('expr_tree_random', format='png', view=True)    
