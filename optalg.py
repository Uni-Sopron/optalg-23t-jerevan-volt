from typing import Set


class Graph:
    def __init__(self) -> None:
        self.data = {}
        self.bus = {}
        self.bus_taken = False

    def add_vertex(self, vertex_name: str):
        for other_vertex in self.data:
            self.data[other_vertex][vertex_name] = None
            self.bus[other_vertex][vertex_name] = False

        self.data[vertex_name] = {vertex: None for vertex in self.data}
        self.data[vertex_name][vertex_name] = None
        self.bus[vertex_name] = {vertex: False for vertex in self.bus}
        self.bus[vertex_name][vertex_name] = False

    def add_arc(self, from_vertex: str, to_vertex: str, weight: float = 1, bus=False):
        if from_vertex in self.data.keys() and to_vertex in self.data.keys():
            self.data[from_vertex][to_vertex] = weight
            if bus: self.bus[from_vertex][to_vertex] = True

    def has_arc(self, from_vertex: str, to_vertex: str) -> bool:
        return self.data[from_vertex][to_vertex] is not None

    def get_weight(self, from_vertex: str, to_vertex: str) -> float:
        return self.data[from_vertex][to_vertex]

    def is_bus(self, from_vertex: str, to_vertex: str) -> bool:
        return self.bus[from_vertex][to_vertex]

    def reachable_vertices(self, vertex: str) -> Set[str]:
        self.unreached_vertices = set(self.data.keys())
        self.explore(vertex)
        reachable = set(self.data.keys()) - self.unreached_vertices
        return reachable

    def explore(self, vertex: str):
        if vertex not in self.unreached_vertices:
            return

        self.unreached_vertices.remove(vertex)

        for t in self.unreached_vertices.copy():
            if self.data[vertex][t] is not None:
                if not self.is_bus(vertex, t):
                    self.explore(t)
                elif self.is_bus(vertex, t) and not self.bus_taken:
                    self.explore(t)

    def shortest_time(self, from_vertex: str, to_vertex: str):
        
        reachable = self.reachable_vertices(from_vertex)

        if to_vertex not in reachable:
            print(f"Vertex {to_vertex} is not reachable from {from_vertex}.")
            return

        previous = {vertex: None for vertex in self.data}
        queue = [from_vertex]

        # Szelessegi bejaras

        while queue:
            current = queue.pop(0)

            if current == to_vertex:
                break

            for neighbor in self.data[current]:
                if self.has_arc(current, neighbor):
                    if previous[neighbor] is None:
                        if self.is_bus(current, neighbor):
                            if not self.bus_taken:
                                self.bus_taken = True
                            else:
                                continue
                        previous[neighbor] = current
                        queue.append(neighbor)


        if previous[to_vertex] is None:
            print(f"Vertex {to_vertex} is not reachable from {from_vertex}.")
            return
        
        # Az ut osszeallitasa

        time = 0
        path = []
        current_vertex = to_vertex

        while current_vertex != from_vertex:
            path.insert(0, current_vertex)
            time += self.get_weight(previous[current_vertex], current_vertex)
            current_vertex = previous[current_vertex]

        path.insert(0, from_vertex)
        path_str = " -> ".join(path)
        print(f"The shortest time is {time} minutes from {from_vertex} to {to_vertex}.")
        print(f"The path is: {path_str}")


# # Test graph
# graph = Graph()

# for i in "JABCDV":
#     graph.add_vertex(i)

# graph.add_arc('J', 'C', 5)
# graph.add_arc('C', 'A', 9, True)
# graph.add_arc('C', 'B', 10, True)
# graph.add_arc('A', 'V', 1)
# graph.add_arc('B', 'V', 1, True)

# graph.shortest_time('J', 'V')










