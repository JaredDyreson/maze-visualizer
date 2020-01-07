#!/usr/bin/env python3.8

def euclidean_heuristic(*args):

    """
    Distance formula for an arbitrary number of points
    and dimensions in Euclidean space.
    """

    container = []
    for i, point in enumerate(args):
      for j, element in enumerate(point):
        try: container[j]
        except IndexError: container.append([])
        container[j].append(element)
    for i, element in enumerate(container):
        container[i] = diffr(element)
    return (sum(container))**0.5
