class BinarySearchTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.node_count = 0

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = BinarySearchTree(value)
                    self.node_count += 1
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = BinarySearchTree(value)
                    self.node_count += 1
                else:
                    self.right.insert(value)
        else:
            self.value = value
            self.node_count += 1

    def show_inorder(self):
        if self.left:
            self.left.show_inorder()
        print(self.value, end=' ')
        if self.right:
            self.right.show_inorder()

    def search(self, value):
        if value < self.value:
            if self.left is None:
                return False
            return self.left.search(value)
        elif value > self.value:
            if self.right is None:
                return False
            return self.right.search(value)
        else:
            return True

    def find_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.value

    def find_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.value
    
    def get_node_count(self):
        # 如果當前節點有值，算作 1 個，否則為 0
        count = 1 if self.value is not None else 0
        # 如果有左邊，加上左邊的總節點數
        if self.left:
            count += self.left.get_node_count()
        # 如果有右邊，加上右邊的總節點數
        if self.right:
            count += self.right.get_node_count()
        return count

# Usage example:
# Constructing a BST
bst = BinarySearchTree()
values = [7, 3, 9, 2, 5, 8, 10]
for val in values:
    bst.insert(val)

# Showing the inorder traversal of the BST
bst.show_inorder()

print(" ")

# Searching for a value
print(bst.search(5))
print(bst.search(6))

print("最小值：",bst.find_min())
print("最大值：",bst.find_max())
print("節點數量：", bst.get_node_count())