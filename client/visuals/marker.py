from pyglet.gl import *


def create_line(one, two, color):
    return 2, GL_LINES, None, ('v2i', (one[0], one[1], two[0], two[1])), ('c3B', color+color)


def create_point(coord, color):
    return 1, pyglet.gl.GL_POINTS, None, ('v2i', (coord[0], coord[1])), ('c3B', color+color)
