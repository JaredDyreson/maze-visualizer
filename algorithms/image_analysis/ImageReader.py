#!/usr/bin/env python3.8

from PIL import Image
from Matrix import Matrix
from Graph import Graph
import os

class ImageParser():
    def __init__(self, path_to_image: str):
        BLACK = (255, 255, 255)
        if not (os.path.exists(path_to_image)): raise FileNotFoundError
        image = Image.open(path_to_image)
        self.rgb_array = image.convert('RGB')
        self.height, self.width = self.rgb_array.size
        # please move empty_matrix to matrix class!!!!!
        self.matrix = Graph({}).empty_matrix(self.height, self.width)

        for x, outer_layer in enumerate(self.matrix):
          for y, element in enumerate(outer_layer):
            r, g, b = self.rgb_array.getpixel((x, y))
            RGB_TUPLE = (r, g, b)
            if(RGB_TUPLE == BLACK): self.matrix[x][y] = 1

i = ImageParser("maze_pictures/small_maze.jpg")
