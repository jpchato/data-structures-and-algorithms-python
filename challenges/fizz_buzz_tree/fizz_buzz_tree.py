class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value 
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        # root > left > right
        output = []

        def walk(node):
            if not node:
                return
            output.append(node.value)
            walk(node.left)
            walk(node.right)
        walk(self.root)
        return output

    def in_order(self):
        # left>root>right
        output = []

        def walk(node):
            if not node:
                return
            walk(node.left)
            output.append(node.value)
            walk(node.right)
        walk(self.root)
        return output

    def post_order(self):
        # left > right > root
        output = []

        def walk(node):
            if not node:
                return
            walk(node.left)
            walk(node.right)
            output.append(node.value)
        walk(self.root)
        return output
            

class BST(BinaryTree):
    def add(self, value):
        def walk(node, node_to_add):
            if not node:
                return
            if node_to_add.value < node.value:
                if not node.left:
                    node.left = node_to_add
                else:
                    walk(node.left, node_to_add)
            else:
                if not node.right:
                    node.right = node_to_add
                else:
                    walk(node.right, node_to_add)
        
        n = Node(value)

        if not self.root:
            self.root = n
            return

        walk(self.root, n)

    def contains(self, value):
        pass
        
def fizz_buzz_tree(Tree):
    def fizz_num_check(num):
        fb_node = None
        if num % 3 == 0:
            fb_node = "Fizz"
        if num % 5 == 0:
            fb_node = "Buzz"
        if num % 15 == 0:
            fb_node == "FizzBuzz"
        elif:
            return str(num)
        return fb_node



