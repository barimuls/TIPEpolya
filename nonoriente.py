import cProfile
import collections
import itertools
import random

# Renvoie un label approximant les orbites d'un graphe non orienté (pas injectif car hash)
#On doit hash pour avoir un int et pas un couple
def invariant_labels(graph, n):
    labels = [1] * n
    for r in range(2):
        neighbor_sums = [0] * n
        for i, j in graph:
            neighbor_sums[i] += labels[j]
            neighbor_sums[j] += labels[i]
        for i in range(n):
            labels[i] = hash(neighbor_sums[i])
    return labels

def inverse_permutation(perm):
    n = len(perm)
    inverse = [None] * n
    for i in range(n):
        inverse[perm[i]] = i
    return inverse

def label_sorting_permutation(labels):
    return inverse_permutation(sorted(range(len(labels)), key=lambda i: labels[i]))

# Applique une permutation à un graphe non orienté
def permuted_graph(perm, graph):
    perm_graph = [(min(perm[i], perm[j]), max(perm[i], perm[j])) for (i, j) in graph]
    perm_graph.sort()
    return perm_graph

def label_stabilizer(labels):
    factors = (
        itertools.permutations(block)
        for (_, block) in itertools.groupby(range(len(labels)), key=lambda i: labels[i])
    )
    for subperms in itertools.product(*factors):
        yield [i for subperm in subperms for i in subperm]

def canonical_graph(graph, n):
    labels = invariant_labels(graph, n)
    sorting_perm = label_sorting_permutation(labels)
    graph = permuted_graph(sorting_perm, graph)
    labels.sort()
    return max(
        (permuted_graph(perm, graph), perm[sorting_perm[n - 1]])
        for perm in label_stabilizer(labels)
    )

def graph_stabilizer(graph, n):
    return [
        perm
        for perm in label_stabilizer(invariant_labels(graph, n))
        if permuted_graph(perm, graph) == graph
    ]

def power_set(n):
    for r in range(n + 1):
        for s in itertools.combinations(range(n), r):
            yield list(s)

def permuted_set(perm, s):
    perm_s = [perm[i] for i in s]
    perm_s.sort()
    return perm_s

def set_stabilizer(s, group):
    stabilizer = []
    for perm in group:
        perm_s = permuted_set(perm, s)
        if perm_s < s:
            return None
        if perm_s == s:
            stabilizer.append(perm)
    return stabilizer

# Générateur des représentants de classes d'isomorphisme de graphes non orientés
def enumerate_graphs(n):
    assert n >= 0
    if n == 0:
        yield []
        return
    for subgraph in enumerate_graphs(n - 1):
        sub_stab = graph_stabilizer(subgraph, n - 1)
        for neighbors in power_set(n - 1):
            stab = set_stabilizer(neighbors, sub_stab)
            if not stab:
                continue
            new_edges = [(min(i, n - 1), max(i, n - 1)) for i in neighbors]
            graph, i_star = canonical_graph(subgraph + new_edges, n)
            if i_star == n - 1:
                yield graph
