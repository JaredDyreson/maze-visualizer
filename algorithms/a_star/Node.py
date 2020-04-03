#!/usr/bin/env python3.8

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        if(position is not None):
          self.x = self.position[0]
          self.y = self.position[1]
        else:
          self.x = None
          self.y = None

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
    def __add__(self, other: tuple) -> tuple:
        coordinate = (
                    self.x + other[0],
                    self.y + other[1]
        )
        return coordinate
