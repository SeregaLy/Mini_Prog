# Поиск в ширину — это алгоритм поиска по графу, который можно использовать
# для решения множества задач, таких как:

# нахождение всех вершин, достижимых из вершины
# найти, связен ли неориентированный граф
# нахождение кратчайшего пути из одной вершины во все остальные вершины
# определить, является ли граф двудольным
# связать диаметр неориентированного графа
# разбиение графа

class Queue():
    def __init__(self):
        self.size = 0
        self.list = []

    def enqueue(self, data):
        self.list.append(data)
        self.size += 1

    def dequeue(self):
        try:
            self.size -= 1
            return self.list.pop(0)
        except Exception as error:
            print(f'{error} is not possible')

    def xprint(self, index):
        print(self.list[index])

    def breadth_first(graph, root):  # поиск в ширину

        queue = Queue()  # очередь для поиска в ширину
        visited_nodes = list()  # список посещенных вершин
        queue.enqueue(root)  # добавляем в очередь начальную вершину
        visited_nodes.append(root)  # добавляем в список посещенных вершин
        current_node = root  # изменяем начальную вершину

        while queue.size > 0:  # пока очередь не пуста
            current_node = queue.dequeue()  # извлекаем вершину из очереди
            adj_nodes = graph[current_node]  # извлекаем список вершин из графа
            remaining_elements = sorted(set(adj_nodes) - set(
                visited_nodes))  # извлекаем список вершин, которые еще не посещены

            if len(remaining_elements) > 0:  # если есть вершины, которые еще не посещены
                for element in remaining_elements:  # добавляем в список посещенных вершин
                    visited_nodes.append(
                        element)  # добавляем в список посещенных вершин
                    queue.enqueue(element)  # добавляем в очередь новую вершину

        return visited_nodes  # возвращаем список посещенных вершин


if __name__ == '__main__':
    graph = dict()

    graph['A'] = ['B', 'G', 'D']
    graph['B'] = ['A', 'F', 'E']
    graph['C'] = ['F', 'H']
    graph['D'] = ['F', 'A']
    graph['E'] = ['B', 'G']
    graph['F'] = ['B', 'D', 'C']
    graph['G'] = ['A', 'E']
    graph['H'] = ['C']

    print(breadth_first(graph, 'A'))
