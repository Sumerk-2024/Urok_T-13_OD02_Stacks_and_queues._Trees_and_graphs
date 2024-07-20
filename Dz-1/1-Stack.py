class Stack:
    def __init__(self):
        # Инициализируем пустой список для хранения элементов стека
        self.items = []

    def is_empty(self):
        # Проверяем, пуст ли стек
        return not self.items

    def push(self, item):
        # Добавляем элемент на вершину стека
        self.items.append(item)

    def pop(self):
        # Удаляем и возвращаем элемент с вершины стека
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        # Возвращаем элемент с вершины стека без удаления
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        # Возвращаем количество элементов в стеке
        return len(self.items)


# Пример использования:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
print(stack.pop())  # Output: 7
print(stack.peek())  # Output: 6
print(stack.size())  # Output: 6
