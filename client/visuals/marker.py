from pyglet.gl import *


def create_line(one, two, color):
    return 2, GL_LINES, None, ('v2i', (one[0], one[1], two[0], two[0])), ('c3B', color+color)
