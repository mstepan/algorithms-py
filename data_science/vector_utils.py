
from __future__ import division
from functools import reduce
import math


def vector_add(vec1, vec2):
    """ add two vectors """
    return [value1 + value2 for value1, value2 in zip(vec1, vec2)]


def vector_subtract(vec1, vec2):
    """ subtract two vectors """
    return [value1 - value2 for value1, value2 in zip(vec1, vec2)]


def scalar_multiply(vec, scalar):
    """ multiple vector by scalar """
    return [value * scalar for value in vec]


def vector_sum(vectors):
    """ add pairwise all vectors """
    return reduce(vector_add, vectors)


def vector_mean(vectors):
    """ pairwise mean value for each vector element """
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))


def dot(vec1, vec2):
    """ dot product of two vectors:  v1*w1 + v2*w2 + ... + vn*wn """
    return sum([x * y for x, y in zip(vec1, vec2)])


def sum_of_squares(vec):
    """
    sum of squares:  v1*v1 + v2*v2 + .. + vn*wn
    """
    return dot(vec, vec)


def magnitude(vec):
    return math.sqrt(sum_of_squares(vec))


def squared_distance(vec1, vec2):
    return sum_of_squares(vector_subtract(vec1, vec2))


def distance(vec1, vec2):
    return magnitude(vector_subtract(vec1, vec2))



