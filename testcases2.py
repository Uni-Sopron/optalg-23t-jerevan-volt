from optalg2 import *
import random

def generate_test_case():
    graph = Graph2()

    for vertex in "ABCD":
        graph.add_vertex(vertex)

    arcs = [
        ("A", "B", random.randint(1, 10), random.choice([True, False])),
        ("A", "C", random.randint(1, 10), random.choice([True, False])),
        ("B", "D", random.randint(1, 10), random.choice([True, False])),
        ("C", "D", random.randint(1, 10), random.choice([True, False]))
    ]

    for arc in arcs:
        from_vertex, to_vertex, weight, bus = arc
        graph.add_arc(from_vertex, to_vertex, weight, bus)

    return graph

graph = generate_test_case()

start_vertex = "A"
end_vertex = "D"

graph.find_shortest_path(start_vertex, end_vertex)
