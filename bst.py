class Node:
    def __init__(self, value, parent = None, left = None, right = None):
        # self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def insert(self, node):
        if self.value >= node.value:
            if self.left:
                self.left.insert(node)
            else:
                self.left = node
        else:
            if self.right:
                self.right.insert(node)
            else:
                self.right = node

    def search (self, value):
        if self.value == value:
            return self
        elif self.value >= value:
            if self.left:
                return self.left.search(value)
            else:
                return None
        else:
            if self.right:
                return self.right.search(value)
            else:
                return None

    def transplant(self, original, replacement):
        if original == original.parent.left:
            original.parent.left = replacement
        else:
            original.parent.right = replacement


    def getVal(self):
        return self.value


class BST:
    def __init__(self, root = None):
        self.root = root

    def insert(self, node):
        if self.root:
            self.root.insert(node)
        else:
            self.root = node

    def search(self, value):
        return self.root.search(value)

    def delete(self, value):
        n = self.search(value)



