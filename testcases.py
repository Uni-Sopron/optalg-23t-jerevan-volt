from optalg import *
import random

def generate_test_case(num_vertices: int, num_arcs: int):
    graph = Graph()

    start_vertex = "J"
    end_vertex = "V"
    graph.add_vertex(start_vertex)
    graph.add_vertex(end_vertex)

    for vertex in range(num_vertices):
        graph.add_vertex(str(vertex))

    vertices = list(graph.data.keys())
    for _ in range(num_arcs):
        from_vertex = random.choice(vertices)
        to_vertex = random.choice(vertices)
        weight = random.randint(1, 10)
        bus = random.choice([True, False])
        graph.add_arc(from_vertex, to_vertex, weight, bus)

    random_vertex = random.choice(vertices)
    graph.add_arc(start_vertex, random_vertex, random.randint(1, 10))
    random_vertex = random.choice(vertices)
    graph.add_arc(random_vertex, end_vertex, random.randint(1, 10))

    return graph, start_vertex, end_vertex

graph, start_vertex, end_vertex = generate_test_case(8, 10)
graph.shortest_time(start_vertex, end_vertex)
