#!/usr/bin/env python3.8


class Matrix:
    def __init__(self, raw_matrix: list):
        self.grid = raw_matrix
        self.height, self.width = self.matrix_height(), self.matrix_width()

    def get_value(self, coordinate: tuple) -> int:
        x_value, y_value = coordinate[0], coordinate[1]
        return self.grid[x_value][y_value]
    
    def set_value(self, coordinate: tuple, value: int) -> None:
        x_value, y_value = coordinate[0], coordinate[1]
        if((x_value > self.height) or (y_value > self.width)):
          raise IndexError("Cannot insert at ({}, {})".format(x_value, y_value))
        else: self.grid[x_value][y_value] = value

    def matrix_height(self) -> int:
        return len(self.grid[0])

    def matrix_width(self) -> int:
        return len(self.grid)
