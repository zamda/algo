from builtins import print
import sys


def read_input(file):
    adjacency_list = {}

    with open(file) as f:
        content = f.readlines()
    for line in content:
        line_split = line.split()
        vertex = int(line_split[0])
        adjacency_list[vertex] = []
        for ind in range(1, len(line_split)):
            edge, weight = line_split[ind].split(",")
            adjacency_list[vertex].append((int(edge), int(weight)))
    return adjacency_list


def run_dijkstra(graph, source_vertex):
    processed_verticies = set()
    processed_verticies.add(source_vertex)
    shortest_path_distances = {}
    shortest_path_distances[source_vertex] = 0

    while len(processed_verticies) != len(graph):
        candidate = source_vertex
        min_cost = sys.maxsize
        for v in processed_verticies:
            for neighbour, cost in graph[v]:
                if neighbour in processed_verticies:
                    continue
                cost_to_neighbour = shortest_path_distances[v] + cost
                if cost_to_neighbour < min_cost:
                    min_cost = cost_to_neighbour
                    candidate = neighbour
        processed_verticies.add(candidate)
        shortest_path_distances[candidate] = min_cost
    return shortest_path_distances

def run(input_file):
    adjacency_list = read_input(input_file)
    distances = run_dijkstra(adjacency_list, 1)
    return distances

def print_distances(distances, ordering):
    if len(ordering) == 0:
        ordering = [x for x in range(1, len(distances) + 1)]

    for i in ordering:
        print(distances[i])


distances = run("dijkstraData.txt")

order = [7,37,59,82,99,115,133,165,188,197]
print_distances(distances, order)
