# Enter you module contents here
"""Module that contains two functions: hypothenuse and area.
"""
__author__ = "Matias Risaro"
__version__ = '1.0.0'

import math

def hypothenuse(b,h):
    """Returns the hypothenuse of a right-triangle.

    Parameters:
       b:  triangle's base.
       h: traingle's height.

    Returns:
       hypothenuse (float)
    """
    return math.sqrt(b**2+h**2)

def area(b,h):
    """Returns the area of a right-triangle.

    Parameters:
       b:  triangle's base.
       h: traingle's height.

    Returns:
       area = b*h/2 (float)
    """
    return b*h/2
