class TreeNode:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None


class BinaryTee:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def insert(self, value):
        def insert_recursive(node, value):
            if not node:
                return TreeNode(value)
            if value < node.value:
                node.left = insert_recursive(node.left, value)
            elif value > node.value:
                node.right = insert_recursive(node.right, value)
            return node

        self.root = insert_recursive(self.root, value)

    def search(self, value):
        def search_recursive(node, value):
            if not node:
                return False
            if node.value == value:
                return True
            elif value < node.value:
                return search_recursive(node.left, value)
            else:
                return search_recursive(node.right, value)

        return search_recursive(self.root, value)

    def delete(self, value):
        def delete_recursive(node, value):
            if not node:
                return node
            if value < node.value:
                node.left = delete_recursive(node.left, value)
            elif value > node.value:
                node.right = delete_recursive(node.right, value)
            else:
                if not node.left and not node.right:
                    return None
                elif not node.left:
                    return node.right
                elif not node.right:
                    return node.left

                temp = self.find_min(node.right)
                node.value = temp.value
                node.right = delete_recursive(node.right, temp.value)
            return node

        self.root = delete_recursive(self.root, value)

    def find_min(self, node):
        while node.left:
            node = node.left
        return node

    def preorder_traversal(self):
        stack = [self.root]
        result = []
        while stack:
            node = stack.pop()
            if node:
                result.append(node.value)
                stack.append(node.right)
                stack.append(node.left)
        return result

    def inorder_traversal(self):
        stack = []
        result = []
        current = self.root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.value)
            current = current.right
        return result

    def postorder_traversal(self):
        stack = [self.root]
        result = []
        while stack:
            node = stack.pop()
            if node:
                result.append(node.value)
                stack.append(node.left)
                stack.append(node.right)

        return result[::-1]


tree = BinaryTee(10)
tree.insert(5)
tree.insert(15)
tree.insert(2)
tree.insert(7)
tree.insert(12)
tree.insert(20)

print("탐색 (7):", tree.search(7))
print("탐색 (17):", tree.search(17))

tree.delete(15)

print("전위 순회:", tree.preorder_traversal())
print("중위 순회:", tree.inorder_traversal())
print("후위 순회:", tree.postorder_traversal())
