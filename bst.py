class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data: int):
        if self.data:
            if data < self.data:
                if not self.left:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if not self.right:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print(self):
        if self.left:
            self.left.print()
        print(self.data)
        if self.right:
            self.right.print()


if __name__ == "__main__":
    bst = Node(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(14)
    bst.insert(17)
    bst.print()
