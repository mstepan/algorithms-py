from __future__ import division
from data_science.stat import *


def error(pipeline, x_i, y_i):
    return y_i - pipeline.predict(x_i)


def predict_y(alpha, betas, x_values):
    return alpha + sum([b_i * x_i for b_i, x_i in zip(betas, x_values)])


def variance_2(pipeline, x, y):
    n = len(y)
    p = len(x[0])
    return sse(pipeline, x, y) / (n - p)


def standard_error(pipeline, x, y, x_single):
    x_mean = mean(x_single)

    # numerator = variance([error(pipeline, x_i, y_i) for x_i, y_i in zip(x, y)])
    numerator = variance_2(pipeline, x, y)
    denominator = sum([(x_i - x_mean) ** 2 for x_i in x_single])

    return math.sqrt(numerator / denominator)


def t_stat(pipeline, beta_single, x, y, x_single):
    return (beta_single - 0.0) / standard_error(pipeline, x, y, x_single)


def p_value(pipeline, alpha, betas, beta_single, x, y, x_single):
    t_stat_value = t_stat(pipeline, beta_single, x, y, x_single)

    p_freq = 0

    betas_copy = []

    for val in betas:
        if val == beta_single:
            betas_copy.append(0)
        else:
            betas_copy.append(val)

    for x_i, y_i in zip(x, y):
        if predict_y(alpha, betas_copy, x_i) >= t_stat_value:
            p_freq += 1

    return p_freq / len(x)


def sse(pipeline, x, y):
    return sum([(y_i - pipeline.predict(x_i)) ** 2 for x_i, y_i in zip(x, y)])


def rse(pipeline, x, y):
    """
    RSE: residual standard error
    """
    p = len(x[0])
    n = len(x)
    return math.sqrt(rss(pipeline, x, y) / (n - p - 1))


def r_squared(pipeline, x, y):
    """
    R^2 statistic, determine how well model fit. Values: [0; 1], 1- means fit 100%
    """
    return 1.0 - (rss(pipeline, x, y) / tss(y))


def f_stat(pipeline, x, y):
    """
    F-statistic, determine dependencies between 'x' and 'y'.
    If 'f-stat' is small (~1) - no dependency between 'x' and 'y'
    """
    p = len(x[0])
    n = len(y)

    rss_val = rss(pipeline, x, y)

    return ((tss(y) - rss_val) / p) / (rss_val / (n - p - 1))


def tss(y):
    y_avg = mean(y)
    return sum([(y_i - y_avg) ** 2 for y_i in y])


def rss(pipeline, x, y):
    """
    RSS: residual sum of squares
    """
    return sum([(y_i - pipeline.predict(x_values)) ** 2 for x_values, y_i in zip(x, y)])


def mse(pipeline, x, y):
    """
    Mean Squared Error (MSE)
    """
    n = len(y)
    return rss(pipeline, x, y) / n



