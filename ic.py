

import itertools


# graph = {
#     0: (1, 4),
#     1: (0, 2, 3),
#     2: (1, 3),
#     3: (1, 2, 4),
#     4: (0, 3)
# }
graph = {
    0: (1,2,3),
    1: (0, 2),
    2: (0,1, 3),
    3: (0, 2),
}

induced = {1: (2, 3), 2: (1, 3), 3: (2, 3)}
# ((0, 1), (1, 2), (1, 3), (2, 3), (3, 4), (4, 0))
#  [[0, 1, 0, 0, 1],
#          [1, 0, 1, 1, 0],
#          [0, 1, 0, 1, 0],
#          [0, 1, 1, 0, 1],
#          [1, 0, 0, 1, 0]]
k = 2


def compress(graph, k, marked):
    res = [com for sub in range(k+1)
           for com in itertools.combinations(marked, sub + 1)]
    for i in res:
        new_marked = set(i)
        for vertex in graph:
            if (vertex) in new_marked:
                continue
            else:
                for edge in graph[vertex]:
                    if edge in graph:
                        if edge not in new_marked:
                            new_marked.add(vertex)
        if len(new_marked) == k:
            correct = True
            for vertex in graph:
                if vertex not in new_marked:
                    for edge in graph[vertex]:
                        if edge not in new_marked:
                            correct = False
            if correct:
                print("marked", new_marked)
                return new_marked
    return False


def iterativeCompression(graph, k):
    marked = range(k+1)
    induced = {}
    for v in range(k+1):
        induced[v] = graph[v]
    for i in range(k+1, len(graph)):
        print("induced", induced)
        marked = compress(induced, k, marked)
        if not marked:
            print("NOT POSSIBLE")
            return False
        induced[i] = graph[i]
    return True


# print(list(range(3)))
# compress(induced, 2, [1,2,3])
print(iterativeCompression(graph, 2))
print(len(graph))