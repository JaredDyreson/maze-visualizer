#!/usr/bin/env python3.8

import enum

class Color(enum.Enum):

    """
    An enum class for colors
    """

    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    ORANGE = (255, 128, 0)
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
