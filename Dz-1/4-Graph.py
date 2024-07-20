class Graph:
    def __init__(self):
        # Инициализируем пустой граф
        self.graph = {}

    def add_edge(self, node, neighbor):
        # Добавляем ребро между двумя вершинами
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

    def print_graph(self):
        # Печатаем граф в виде списка смежности
        for node in self.graph:
            print(f"{node} -> {' -> '.join(map(str, self.graph[node]))}")

    def bfs(self, start):
        # Обход графа в ширину (BFS)
        visited = set()
        queue = [start]

        while queue:
            node = queue.pop(0)
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                queue.extend([neighbor for neighbor in self.graph.get(node, []) if neighbor not in visited])
        print()  # для перехода на новую строку после завершения обхода

    def dfs(self, start, visited=None):
        # Обход графа в глубину (DFS)
        if visited is None:
            visited = set()
        if start not in visited:
            print(start, end=" ")
            visited.add(start)
            for neighbor in self.graph.get(start, []):
                if neighbor not in visited:
                    self.dfs(neighbor, visited)
        if start == list(self.graph.keys())[0]:  # проверка на первый вызов для новой строки
            print()  # для перехода на новую строку после завершения обхода


# Пример использования:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(2, 6)
g.add_edge(3, 7)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(3, 0)
g.add_edge(4, 6)

g.print_graph()

print("BFS traversal starting from vertex 2:")
g.bfs(2)  # Output: 2 0 3 1

print("DFS traversal starting from vertex 2:")
g.dfs(2)  # Output: 2 0 1 3
