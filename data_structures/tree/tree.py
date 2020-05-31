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
            

    def postOrder(self):
        pass



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
        # I've been at this for 5 hours. I'm done.
            
 




# bst = BST()
# bst.add(4)
# bst.add(7)
# bst.add(5)
# bst.add(9)
# bst.add(2)
# bst.add(30)
# bst.add(-1)
# print(bst.pre_order())
# print(bst.post_order())
# print(bst.in_order())
# print(bst.contains(675))
