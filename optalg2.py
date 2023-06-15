class Graph:
    def __init__(self) -> None:
        self.data = {}
        self.bus = {}

    def add_vertex(self, vertex_name: str):
        self.data[vertex_name] = {}
        self.bus[vertex_name] = {}

    def add_arc(self, from_vertex: str, to_vertex: str, weight: float, bus=False):
        if from_vertex in self.data and to_vertex in self.data:
            self.data[from_vertex][to_vertex] = weight
            self.bus[from_vertex][to_vertex] = bus

    def has_arc(self, from_vertex: str, to_vertex: str) -> bool:
        return from_vertex in self.data and to_vertex in self.data[from_vertex]

    def get_weight(self, from_vertex: str, to_vertex: str) -> float:
        return self.data[from_vertex][to_vertex]

    def bfs(self, start_vertex: str, end_vertex: str):
        if start_vertex not in self.data or end_vertex not in self.data:
            return {}

        visited = set()
        queue = [(start_vertex, 0, None, 0, False)]  # (vertex, cost, previous_vertex, bus, bus_taken)
        path_costs = {start_vertex: (0, None, 0, False)}  # vertex: (cost, previous_vertex, bus, bus_taken)

        while queue:
            vertex, cost, previous_vertex, bus_arc, bus_taken = min(queue, key=lambda item: item[1])
            queue.remove((vertex, cost, previous_vertex, bus_arc, bus_taken))

            if vertex in visited:
                continue

            visited.add(vertex)

            for neighbor, weight in self.data[vertex].items():
                if neighbor not in visited:
                    total_cost = cost + weight
                    is_bus = self.bus[vertex][neighbor]
                    if neighbor not in path_costs or total_cost < path_costs[neighbor][0]:
                        if is_bus and bus_arc >= 1 and bus_taken:
                            continue
                        path_costs[neighbor] = (total_cost, vertex, bus_arc + int(is_bus), bus_taken or is_bus)
                        queue.append((neighbor, total_cost, vertex, bus_arc + int(is_bus), bus_taken or is_bus))

        return path_costs

    def construct_path(self, start_vertex: str, end_vertex: str, path_costs):
        if end_vertex not in path_costs:
            return None

        path = [end_vertex]
        current_vertex = end_vertex

        while current_vertex != start_vertex:
            previous_vertex = path_costs[current_vertex][1]
            if previous_vertex is None:
                return None
            path.append(previous_vertex)
            current_vertex = previous_vertex

        return list(reversed(path))
    
    def get_path_weight(self, path):

        weight = 0
        for i in range(len(path) - 1):
            weight += self.get_weight(path[i], path[i+1])
        return weight

    def find_shortest_path(self, start_vertex, end_vertex):
        path_costs = self.bfs(start_vertex, end_vertex)

        if end_vertex not in path_costs:
            print(f"The vertex '{end_vertex}' is not reachable from '{start_vertex}'.")
            return

        _, _, num_bus_taken, bus_taken = path_costs[end_vertex]

        path = self.construct_path(start_vertex, end_vertex, path_costs)
        path_str = " -> ".join(path)

        if num_bus_taken > 1:
            print(f"The vertex '{end_vertex}' is reachable, but requires more than one bus to take.")
        elif num_bus_taken == 0:
            print(f"The shortest path from '{start_vertex}' to '{end_vertex}' is: {path_str}. It is {self.get_path_weight(path)} minutes.")
        else:
            print(f"The shortest path from '{start_vertex}' to '{end_vertex}' with one bus ride: {path_str}. It will be {self.get_path_weight(path)} minutes.")
