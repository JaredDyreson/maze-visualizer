#!/usr/bin/env python3.8

from Graph import Graph
from pprint import pprint as pp
import numpy as np
from Matrix import Matrix

"""
This was taken from this source and heavily modified

https://rosettacode.org/wiki/A*_search_algorithm#Python

The refactored code was done by Jared Dyreson.
"""

class a_star:
    def __init__(self, matrix: Matrix):
        self.matrix = matrix
        self.matrix_height, self.matrix_width = self.matrix.height, self.matrix.width 
        self.barriers = self.find_barriers()

    def find_barriers(self) -> list:

        """
        Check the matrix for each index
        and append coordinates (tuples) to a list.
        """

        barrier_list = []
        for x, outer_row in enumerate(self.matrix.grid):
          for y, element in enumerate(outer_row):
            if(self.matrix.get_value((x, y)) == 1): barrier_list.append((x, y))
        return barrier_list

    def diffr(self, items: list):

        """
        sum() but for the inverse operation.
        Code found here -> https://stackoverflow.com/questions/9963524/what-is-a-subtraction-function-that-is-similar-to-sum-for-subtracting-items-in
        """

        return items[0] - sum(items[1:])

    def chebyshev_heuristic(self, *args):
      """
      This formula was designed to return
      the Chebychev distance of n number of coordinates of k number of dimensions.
      """

      d = 1 
      container = []
      for i, point in enumerate(args):
       for j, element in enumerate(point):
          try: container[j]
          except IndexError: container.append([])
          container[j].append(element)
      for i, element in enumerate(container):
        container[i] = abs(self.diffr(element))
      return d * (sum(container)) + ((d-2)*d) * min(*container)

    def has_duplicate(self, term: object, container: list) -> bool:

        """
        Given a list, check if there are duplicate elements.
        If return is false, then the list is unique and therefore also a set.
        You can also cast the list into a set and check if the lengths are the same.
        This is not memory efficient.
        """

        counter = 0
        container.sort()
        for element in container:
          if(element == term): counter+=1
          elif(counter > 1): return True
        return False

    def move_cost(self, coordinate_list: list, barriers: list) -> int:

        """
        Determine the cost for movement from point a to an arbitrary number of points.
        Barriers are given a large value to indicate that we are not allowed to enter.
        """

        cost = 0
        for point in coordinate_list[1:]:
          if(point in barriers): cost+=(self.matrix_height * self.matrix_width)
          else: cost+=1
        return cost

    def get_vertex_neighbors(self, coordinate: tuple) -> list:

        """
        Find all the adjacent neighbors for a given point in the matrix.
        This only works in R^2
        """

        possible_avenues = []
        movements = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)] 
        boundary = len(movements)
        
        for dx, dy in movements:
          x_final = coordinate[0] + dx
          y_final = coordinate[1] + dy
          if not ((x_final < 0) or (x_final > boundary) or (y_final < 0) or (y_final > boundary)):
            possible_avenues.append((x_final, y_final))
        return possible_avenues

    def search(self, start: tuple, end: tuple) -> tuple:
        print(self.barriers)
        movement_cost = {} 
        estimated_cost =  {}

        movement_cost[start] = 0
        estimated_cost[start] = self.chebyshev_heuristic(start, end)

        closed_verticies = set()
        open_verticies = set([start])
        came_from = {}

        while len(open_verticies) > 0:
          current = None
          current_f_score = None
          for position in open_verticies:
            if((current is None) or (estimated_cost[position] < current_f_score)):
              current_f_score = estimated_cost[position]
              current = position

          if(current == end):
            path = [current]
            while current in came_from:
              current = came_from[current]
              path.append(current)
            path.reverse()
            return (path, estimated_cost[end])

          open_verticies.remove(current)
          closed_verticies.add(current)

          for neighbor in self.get_vertex_neighbors(current):
            if (neighbor in closed_verticies):
              continue
            candidate_g = movement_cost[current] + self.move_cost([current, neighbor], self.barriers)
            if (neighbor not in open_verticies):
              open_verticies.add(neighbor)
            elif(candidate_g >= movement_cost[neighbor]):
              continue

            came_from[neighbor] = current     
            movement_cost[neighbor] = candidate_g
            H = self.chebyshev_heuristic(neighbor, end)
            estimated_cost[neighbor] = movement_cost[neighbor] + H
        raise RuntimeError("A* cannot find solution")


    def paint_path(self, path: list) -> None:

        """
        Iterate over a matrix and change the coordinates to a value of five.
        Five indicates to our draw function to paint it blue.
        """

        for point in path:
          self.matrix.set_value((point[0], point[1]), 4)
