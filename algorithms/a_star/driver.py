#!/usr/bin/env python3.8

from Window import Window
from Graph import Graph
from a_star import a_star
import json

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
        return Graph({}).empty_matrix(9, 9)

grid = load_grid("../../matricies/matrix_test.txt")
algo = a_star(grid)
path, cost = algo.search((0, 0), (8, 8))
algo.paint_path(path)

w = Window(grid, "Maze Solving", [255,255], 23, 23, 5)
w.run()
# w.save_grid("../../matricies/matrix_test.txt")
