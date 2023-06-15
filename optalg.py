from collections import defaultdict


class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = defaultdict(dict)

    def add_vertex(self, vertex):
        self.vertices.add(vertex)

    def add_edge(self, from_vertex, to_vertex, weight, color='blue'):

        if from_vertex not in self.vertices or to_vertex not in self.vertices:
            raise ValueError("One or both vertices do not exist in the graph.")

        self.edges[from_vertex][to_vertex] = {'weight': weight, 'color': color}

    def has_edge(self, from_vertex, to_vertex):
        return to_vertex in self.edges[from_vertex]

    def get_weight(self, from_vertex, to_vertex):
        return self.edges[from_vertex][to_vertex]['weight']

    def get_color(self, from_vertex, to_vertex):
        return self.edges[from_vertex][to_vertex]['color']

    def dfs(self, start, visited=None, red_edge_taken=False):

        if visited is None: visited = set()

        visited.add(start)

        for neighbor in self.edges[start]:
            if neighbor not in visited:
                edge_color = self.get_color(start, neighbor)
                if not red_edge_taken or (red_edge_taken and edge_color != 'red'):
                    red_edge_taken_new = red_edge_taken or edge_color == 'red'
                    self.dfs(neighbor, visited, red_edge_taken_new)

    def get_path_weight(self, path):

        weight = 0
        for i in range(len(path) - 1):
            weight += self.get_weight(path[i], path[i+1])
        return weight

    def shortest_path(self, start, end, visited=None, red_edge_taken=False):

        if visited is None: visited = set()

        visited.add(start)

        if start == end: 
            return [end]

        if start not in self.vertices or end not in self.vertices:
            return None

        shortest = None

        for neighbor in self.edges[start]:
            if neighbor not in visited:
                edge_color = self.get_color(start, neighbor)
                if not red_edge_taken or (red_edge_taken and edge_color != 'red'):
                    red_edge_taken_new = red_edge_taken or edge_color == 'red'
                    new_path = self.shortest_path(neighbor, end, visited.copy(), red_edge_taken_new)
                    if new_path:
                        new_path.insert(0, start)
                        if shortest is None or self.get_path_weight(new_path) < self.get_path_weight(shortest):
                            shortest = new_path

        return shortest
    
    def print_results(self, from_vertex, to_vertex):

        shortest_path = self.shortest_path(from_vertex, to_vertex)

        if shortest_path:
            path_str = " -> ".join(shortest_path)
            print(f"The shortest path is {path_str} with a weight of {self.get_path_weight(shortest_path)}.")
        else:
            print(f"No path found to {to_vertex} from {from_vertex}.")

