import copy
import random


def read_input(file):
    adjacency_list = {}

    with open(file) as f:
        content = f.readlines()
    for line in content:
        line_split = list(map(lambda x: int(x), line.split()))
        adjacency_list[line_split[0]] = []
        for ind in range(1, len(line_split)):
            adjacency_list[line_split[0]].append(line_split[ind])
    return adjacency_list


def remove_all(iterable, elem):
    return list(filter(lambda x: x != elem, iterable))


def replace_all(iterable, elem, to):
    return list(map(lambda x: to if x == elem else x, iterable))


def find_min_cut(adjacency_list):
    random_v1 = 0
    while len(adjacency_list) > 2:
        #pick an edge to delete uniformly at random
        random_v1 = random.choice(list(adjacency_list.keys()))
        random_v2 = random.choice(adjacency_list[random_v1])

        for val in adjacency_list[random_v2]:
            adjacency_list[val].remove(random_v2)
            adjacency_list[val].append(random_v1)

        adjacency_list[random_v1] += adjacency_list[random_v2]
        adjacency_list[random_v1] = remove_all(adjacency_list[random_v1], random_v1)

        del adjacency_list[random_v2]

    return len(adjacency_list[random_v1])


def find_min_cut_runner(input_list):
    min_cut = len(input_list)
    n = len(input_list)
    for ith in range(10):
        result = find_min_cut(copy.deepcopy((input_list)))
        min_cut = min(min_cut, result)
        print(ith)
    return min_cut


def run(input_file):
    adjacency_list = read_input(input_file)
    result = find_min_cut_runner(adjacency_list)
    return result


print(run("kargerMinCut.txt"))