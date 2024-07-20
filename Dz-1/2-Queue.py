class Queue:
    def __init__(self):
        # Инициализируем пустой список для хранения элементов очереди
        self.items = []

    def is_empty(self):
        # Проверяем, пуста ли очередь
        return not self.items

    def enqueue(self, item):
        # Добавляем элемент в конец очереди
        self.items.insert(0, item)

    def dequeue(self):
        # Удаляем и возвращаем элемент из начала очереди
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def size(self):
        # Возвращаем количество элементов в очереди
        return len(self.items)


# Пример использования:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
print(queue.dequeue())  # Output: 1
