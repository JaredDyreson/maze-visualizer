#!/usr/bin/env python3.8

from Window import Window
from Graph import Graph
from a_star import a_star
import json
from Matrix import Matrix

# Graph components

# graph = {
  # "a": ["b", "c"],
  # "b": ["d"],
  # "c": ["d", "e"],
  # "e": ["f", "g"],
  # "h": ["i"]
# }

# origin = (0, 0)
# end = (1, 1)

# g = Graph(graph, origin, end)

def load_grid(path_to_grid: str) -> list:
  """
  Read in the matrix from a text file.
  Throw exception if the data is malformed.
  """

  with open(path_to_grid) as in_file:
      try:
        return json.loads(in_file.read())
      except json.JSONDecodeError:
        return Graph({}).empty_matrix(100, 100)

grid = Graph({}).empty_matrix(9, 9)
def run_headless():
  matrix = Matrix(grid)

  algo = a_star(matrix)
  path, cost = algo.search((0, 0), (5, 5))
  algo.paint_path(path)
  print("path taken: {}".format(path))

def run_gui():
  w = Window(grid, "Maze Solving", [500, 500], 35, 35, 0)
  w.run()

run_headless()
# run_gui()
# w.save_grid("../../matricies/larger_matrix.txt")
