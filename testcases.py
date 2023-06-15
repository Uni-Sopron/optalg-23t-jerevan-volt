from optalg import *
import random

def generate_test_case(graph, num_vertices, num_edges):

    vertices = [chr(ord('A') + i) for i in range(num_vertices)]

    for vertex in vertices:
        graph.add_vertex(vertex)

    colors = ['red', 'blue']
    
    for _ in range(num_edges):
        from_vertex = random.choice(vertices)
        to_vertex = random.choice(vertices)
        while from_vertex == to_vertex or graph.has_edge(from_vertex, to_vertex):
            from_vertex = random.choice(vertices)
            to_vertex = random.choice(vertices)
        weight = random.randint(1, 10)
        color = random.choice(colors)
        graph.add_edge(from_vertex, to_vertex, weight, color)

    return graph

graph = Graph()

num_vertices = 5
num_edges = 8

test_graph = generate_test_case(graph, num_vertices, num_edges)

from_vertex = 'A'
to_vertex = 'D'

graph.print_results("A", "D")




