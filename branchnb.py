# Artificial Intelligence
# Mariana Chavez
# Jokebed Aguirre
#
# Branch and Bound for Travelling salesman problem

from filecmp import cmp
from queue import *


# creates node
class Node(object):
    def __init__(self, level=None, path=None, bound=None):
        self.level = level
        self.path = path
        self.bound = bound

    def __cmp__(self, other):  # cmp compares two values and returns integer as if true or false
        return cmp(self.bound, other.bound)

    def __str__(self):
        return str(tuple([self.level, self.path, self.bound]))  # tuple is used to store items in a single variable


# function that calculates the best path
# compares the values with 0 being 0 the best way to minimize the matrix
def travel(adj_mat, src=0):
    optimal_tour = []
    n = len(adj_mat)  # this function returns the number of items in adj_mat
    u = Node()
    optimal_length = 0
    v = Node(level=0, path=[0])
    min_length = float('inf')  # infinity
    v.bound = bound(adj_mat, v)  # feasible path
    PriorityQueue().put(v)  # possible solutions
    while not PriorityQueue().empty():
        v = PriorityQueue().get()  # extract the values
        if v.bound < min_length:  # if it is feasible and optimum
            u.level = v.level + 1  # it is a solution so we have to add 1 to the (node) value level
            # helps to filter out all the elements we don't care, for which the function returns True
            for i in filter(lambda x: x not in v.path, range(1, n)):
                u.path = v.path[:]
                u.path.append(i)
                if u.level == n - 2:
                    # it converts to sequence of iterable elements with distinct elements.
                    l = set(range(1, n)) - set(u.path)
                    u.path.append(list(l)[0])
                    # putting the first vertex at last
                    u.path.append(0)

                    _len = length(adj_mat, u)
                    if _len < min_length:
                        min_length = _len
                        optimal_length = _len  # if the length is minor to the minimum length it'll be optimal
                        optimal_tour = u.path[:]  # we add the path of the node to the optimal tour

                # else, node is a single candidate which is not optimum
                else:
                    u.bound = bound(adj_mat, u)
                    if u.bound < min_length:
                        PriorityQueue().put(u)
                u = Node(level=u.level)  # make a new node at each iteration

    # shifting to proper source(start of path)
    optimal_tour_src = optimal_tour
    if src != 1:
        optimal_tour_src = optimal_tour[:-1]
        y = optimal_tour_src.index(src)
        optimal_tour_src = optimal_tour_src[y:] + optimal_tour_src[:y]
        optimal_tour_src.append(optimal_tour_src[0])

    return optimal_tour_src, optimal_length


def length(adj_mat, node):
    tour = node.path
    # returns the sum of two consecutive elements of tour in adj[i][j]
    return sum([adj_mat[tour[i]][tour[i + 1]] for i in range(len(tour) - 1)])


def bound(adj_mat, node) -> object:
    path = node.path
    _bound = 0

    n = len(adj_mat)
    determined, last = path[:-1], path[-1]
    # remain is index based
    remain = filter(lambda x: x not in path, range(n))

    # for the edges that are certain
    for i in range(len(path) - 1):
        _bound += adj_mat[path[i]][path[i + 1]]

    # for the last item
    _bound += min([adj_mat[last][i] for i in remain])

    p = [path[0]] + remain
    # for the undetermined nodes
    for r in remain:
        _bound += min([adj_mat[r][i] for i in filter(lambda x: x != r, p)])
    return _bound


if __name__ == '__main__':
    matrix = [
        [0, 14, 4, 10, 20],
        [14, 0, 7, 8, 7],
        [4, 5, 0, 7, 16],
        [11, 7, 9, 0, 2],
        [18, 7, 17, 4, 0]
    ]

    # print(travel(matrix))
    print(matrix)
    print(travel)
