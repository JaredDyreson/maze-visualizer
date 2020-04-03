#!/usr/bin/env python3.8

# Verticies: nodes on the graph
# Edges: paths connecting each node on the graph

from pprint import pprint as pp
import numpy as np
from typing import Dict
import queue

class Graph:
    """
    This is a graph class that represents a simple graph.
    
    self.mapping -> a dictionary representation of the graph.
                    This is the most human readable version of
                    a graph we can make at the moment.
    self.matrix -> a matrix representation of the graph.
                   This allows us to use numpy and some
                   other linear algebra to solve a given
                   graph or maze.

    Values of the matrix are as follows:
    0: empty and free to move
    1: a barrier, not allowing for movement
    2: starting position of the graph
    3: ending position of the graph
    4: this a connection, therefore a path between two nodes
    """
    def __init__(self, mapping: dict, start=None, end=None):
        self.mapping = mapping
        self.matrix = self.generate_matrix()
        self.start = start
        self.end = end
        self.verticies = self.get_verticies()
        if(start and  end is not None):
          x_naught, y_naught = start[0], start[1]
          x_final, y_final = end[0], end[1]
          self.matrix[x_naught][y_naught] = 2
          self.matrix[x_final][y_final] = 3

    @classmethod
    def complete_graph(cls, verticies: list) -> dict:

      """
      A complete graph is a graph that has every pair of distinct 
      vertices that is connected by a unique edge.
      Given a list of verticies we can construct a mapping of n verticies
      to its neighboring indicies.
      Example: ["a", "b", "c"] translates to the following:

      {
        "a": ["b", "c"],
        "b": ["a", "c"],
        "c": ["a", "b"]
      }

      where the key is not present inside the associate unique list (set)
      """

      G = {}
      if(len(verticies) == 0): return
      for i, v in enumerate(verticies):
       key = verticies[i]
       look_behind = verticies[:i]
       look_ahead = verticies[i:]
       combined = look_behind + look_ahead
       combined.remove(key)
       G[verticies[i]] = combined
      return cls(G)
    def generate_matrix(self) -> list:

      """
      Make the map representation into matrix.
      Generate a blank matrix then you iterate
      over the map, where the keys and value indexes are
      taken into account.
      Each cell that a label is mapped to is iterated over, marking each x and y
      position.
      """

      V = len(self.mapping.items())
      matrix = [[0 for x in range(V)]
              for y in range(V)]
      for x, (v, e) in enumerate(self.mapping.items()):
        for y, node in enumerate(e):
          matrix[x][y] = 4
      return matrix
    def print_graph(self) -> None:
      """
      Here we need to treat the matrix (grid) and the graph (G) as associative entities.
      We use the positions of 1's (possible nodes) mapped to an associative graph.

      Let G = {
        (x = 0) "a": ["b"(y = 0), "c"(y = 1)]
      }

      and the matrix is:

      matrix = [[1, 1]]

      Where matrix[0][0] = "a,b"
            matrix[0][1] = "a,c"
      We use the indexes in the matrix to lookup keys and associated sets to those particular nodes
      """
      V = len(self.mapping.items())
      keys = list(self.mapping.keys())
      for x in range(V):
        for y in range(V):
          if(self.matrix[x][y] == 4):
            key_lookup = keys[x]
            # |E| --> cardinality or amount of elements contained in the list mapped to a given vertice
            # E = len(graph[key_lookup])
            value = self.mapping[key_lookup][y]
            print("{{ {}, {} }}".format(key_lookup, value))

    def get_verticies(self) -> list:
      """
      Grab all the nodes in a given graph
      This is done by getting all the labels
      from the keys and then subsequntely finding
      more nodes inside the list that they are mapped
      to by the parent node.
      """

      v_arr = []
      for v, e in self.mapping.items():
          if v not in v_arr: v_arr.append(v)
          for node in e:
            if node not in v_arr: v_arr.append(node)
      return v_arr

    def empty_matrix(self, size_of_x: int, size_of_y: int) -> list:
       return [[0 for x in range(size_of_x)]
              for y in range(size_of_y)]

        
# grid = Graph({}).empty_matrix(9, 9)
# grid[0][0] = 1
# print(find_barriers(grid))
# quit()
# a_star_search((0, 0), (0, 1), grid)
