import random
from optalg import *
from optalg2 import *
import time

def generate_test_case(num_vertices, num_edges, graph, graph2):

    vertices = [chr(ord('A') + i) for i in range(num_vertices)]
    print(vertices)

    for vertex in vertices:
        graph.add_vertex(vertex)
        graph2.add_vertex(vertex)

    for _ in range(num_edges):
        from_vertex = random.choice(vertices)
        to_vertex = random.choice(vertices)
        while from_vertex == to_vertex or graph.has_edge(from_vertex, to_vertex) or graph2.has_arc(from_vertex, to_vertex):
            from_vertex = random.choice(vertices)
            to_vertex = random.choice(vertices)
        weight = random.randint(1, 10)
        color = random.choice(['blue','red'])
        if color == 'red': bus = True
        else: bus = False

        graph.add_edge(from_vertex, to_vertex, weight, color)
        graph2.add_arc(from_vertex, to_vertex, weight, bus)

    return graph, graph2


graph = Graph()
graph2 = Graph2()

num_vertices = 50
num_edges = 100

generate_test_case(num_vertices, num_edges, graph, graph2)

from_vertex = 'A'
to_vertex = 'r'

start = time.time()
graph.print_results(from_vertex, to_vertex)
end = time.time()

print(f"optalg1 Time: {end-start}")

start2 = time.time()
graph2.find_shortest_path(from_vertex, to_vertex)
end2 = time.time()

print(f"optalg2 Time: {end2-start2}")