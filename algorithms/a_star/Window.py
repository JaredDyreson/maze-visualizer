#!/usr/bin/env python3.8

"""
 Example program to show using an array to back a grid on-screen.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/mdTeqiWyFnc
"""

"""
This has been adapted to work in a class
Written by Jared Dyreson
"""

import pygame
from Graph import Graph
from pprint import pprint as pp
import json
from Color import Color
import numpy as np
import os


class Window:
    def __init__(self, matrix: list, title: str, size: list, 
                    height: int, width: int, margin: int):
        """
        A window class using Pygame
        This is heavily inspired by the Java
        class JFrame.
        """

        self.cell_margin = margin
        self.clock = pygame.time.Clock()
        self.colors = Color
        self.cell_height = height
        self.matrix = matrix
        arr = np.array(self.matrix)
        self.matrix_height, self.matrix_width = arr.shape[0], arr.shape[1]
        self.program_complete = False
        self.screen = pygame.display.set_mode(size)
        if(len(size) == 1): size.append(*size)
        self.size = size
        self.title = title
        self.cell_width = width

        pygame.display.set_caption(self.title)

    def __del__(self):
        """
        Close the window when the destructor is called.
        This makes it idle friendly.
        """

        pygame.quit()

    def load_grid(self, path_to_grid: str) -> None:
      """
      Read in the matrix from a text file.
      Throw exception if the data is malformed.
      """

      with open(path_to_grid) as in_file:
          try:
            self.matrix = json.loads(in_file.read())
          except json.JSONDecodeError:
            self.matrix = Graph({}).empty_matrix(self.size[0], self.size[1])
          self.draw_grid()

    def save_grid(self, path_to_file: str) -> None:
      """
      Save the current matrix to a text file.
      If file exists, raise exception.
      """

      if(os.path.exists(path_to_file)):
        print("[-] File exists at {}".format(path_to_file))
        # raise FileExistsError
      with open(path_to_file, 'w') as out_file:
          out_file.write(str(self.matrix))

    def draw_grid(self) -> None:
      """
      Given a matrix (n > 1 dimensional array), we need to draw those
      cells on the screen.
      This is done by having a nested for loop and depending on the value at
      a given index, we paint the square that particular color.
      The values go as follows:
      0 --> free space, allowing for movement (White)
      1 --> wall, indicating no movement allowed (Black)
      2 --> starting position, also a free space (Green)
      3 --> ending position, also a free space (Red)
      4 --> path color (Blue)
      """
      for row in range(self.matrix_height):
          for column in range(self.matrix_width):
              color = self.colors.WHITE.value
              position = self.matrix[row][column]
              if(position == 0): color = self.colors.WHITE.value
              elif(position == 1): color = self.colors.BLACK.value
              elif(position == 2): color = self.colors.GREEN.value
              elif(position == 3): color = self.colors.RED.value
              elif(position == 4): color = self.colors.BLUE.value

              pygame.draw.rect(self.screen,
                               color,
                               [(self.cell_margin + self.cell_width) * column + self.cell_margin,
                                (self.cell_margin + self.cell_height) * row + self.cell_margin,
                                self.cell_width,
                                  self.cell_height])
    def run(self) -> None:
      """
      Main loop of the program.
      This handles the updating and drawing of the grid.
      Also handles user input and processes it as such.
      """

      while not self.program_complete:
          for event in pygame.event.get():
              if event.type == pygame.QUIT:  
                  self.program_complete = True
              elif event.type == pygame.MOUSEBUTTONDOWN:
                  cursor_position = pygame.mouse.get_pos()
                  column = cursor_position[0] // (self.cell_width + self.cell_margin)
                  row = cursor_position[1] // (self.cell_height + self.cell_margin)
                  self.matrix[row][column] = 1
       
          self.screen.fill(self.colors.BLACK.value)
          self.draw_grid()
          self.clock.tick(60)
          pygame.display.flip()

