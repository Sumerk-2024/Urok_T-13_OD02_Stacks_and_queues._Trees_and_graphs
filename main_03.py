# Бинарное дерево — это вид дерева, в котором каждый узел имеет не более двух потомков.

class Node():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


# Функция для добавления нового узла
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.value < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


root = Node(70)
root = insert(root, 30)
root = insert(root, 56)
root = insert(root, 89)
root = insert(root, 45)
root = insert(root, 60)
root = insert(root, 73)
root = insert(root, 98)
root = insert(root, 84)
