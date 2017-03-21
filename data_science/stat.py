from collections import Counter
from data_science.vector_utils import *

def mean(vec):
    """ average/mean value """
    return sum(vec) / len(vec)


def median(vec):
    sorted_vec = sorted(vec)

    mid = len(vec) // 2

    # odd length case
    if len(vec) & 1 == 1:
        return sorted_vec[mid]

    # even length case
    return (sorted_vec[mid-1] + sorted_vec[mid]) / 2


def quantile(vec, p):
    """ returns the p-th percentile value in vec """

    index = int(len(vec) * p)

    return sorted(vec)[index]


def mode(vec):
    """ most frequent element(s) """

    counters = Counter(vec)
    max_freq = max(counters.values())

    return [value for value, cnt in counters.items() if cnt == max_freq]


def data_range(vec):
    return max(vec) - min(vec)


def de_mean(vec):
    avg = mean(vec)
    return [value - avg for value in vec]


def variance(vec):
    deviations = de_mean(vec)
    return sum_of_squares(deviations) / len(vec)


def standard_deviation(vec):
    return math.sqrt(variance(vec))


def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)


def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / (stdev_x * stdev_y)
    else:
        return 0 # if no variation, correlation is zero
