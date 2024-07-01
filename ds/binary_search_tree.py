class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current, node = self, BST(value=value)
        while True:
            if value < current.value:
                if current.left is None:
                    current.value = node
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.value = node
                    break
                else:
                    current = current.right
        return self
                
    def contain(self, value):
        current = self
        while current is not None:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True
        return False

    def remove(self, value):
        ...