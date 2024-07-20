class Node:
    def __init__(self, key):
        # Инициализируем узел с заданным ключом
        self.left = None
        self.right = None
        self.value = key


class BinaryTree:
    def __init__(self):
        # Инициализируем пустое бинарное дерево
        self.root = None

    def insert(self, key):
        # Вставляем новый узел в дерево
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        # Вспомогательная функция для рекурсивной вставки узла
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def inorder_traversal(self, node):
        # Обход дерева в порядке (inorder): лево -> корень -> право
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=" ")
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        # Обход дерева в прямом порядке (preorder): корень -> лево -> право
        if node:
            print(node.value, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        # Обход дерева в обратном порядке (postorder): лево -> право -> корень
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.value, end=" ")

    def find(self, key):
        # Поиск узла с заданным значением
        return self._find(self.root, key)

    def _find(self, node, key):
        if node is None or node.value == key:
            return node
        if key < node.value:
            return self._find(node.left, key)
        return self._find(node.right, key)

    def delete(self, key):
        # Удаление узла с заданным значением
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.value:
            node.left = self._delete(node.left, key)
        elif key > node.value:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self._min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete(node.right, temp.value)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current


# Пример использования:
tree = BinaryTree()

# Вставляем узлы в дерево
tree.insert(50)
tree.insert(30)
tree.insert(20)
tree.insert(40)
tree.insert(70)
tree.insert(60)
tree.insert(80)

print("Inorder traversal of the given tree:")
tree.inorder_traversal(tree.root)  # Output: 20 30 40 50 60 70 80

print("\nPreorder traversal of the given tree:")
tree.preorder_traversal(tree.root)  # Output: 50 30 20 40 70 60 80

print("\nPostorder traversal of the given tree:")
tree.postorder_traversal(tree.root)  # Output: 20 40 30 60 80 70 50

# Поиск узлов в дереве
print("\n\nFind node with value 20:")
found_node = tree.find(20)
print(found_node.value if found_node else "Not found")  # Output: 20

print("Find node with value 25:")
found_node = tree.find(25)
print(found_node.value if found_node else "Not found")  # Output: Not found

# Удаление узлов из дерева
print("\nDelete node with value 20")
tree.delete(20)
print("Inorder traversal after deleting 20:")
tree.inorder_traversal(tree.root)  # Output: 30 40 50 60 70 80

print("\nDelete node with value 30")
tree.delete(30)
print("Inorder traversal after deleting 30:")
tree.inorder_traversal(tree.root)  # Output: 40 50 60 70 80

print("\nDelete node with value 50")
tree.delete(50)
print("Inorder traversal after deleting 50:")
tree.inorder_traversal(tree.root)  # Output: 40 60 70 80
