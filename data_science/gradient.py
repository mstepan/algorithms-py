import random
from data_science.vector_utils import *


def minimize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
    data = zip(x, y)
    theta = theta_0  # initial guess
    alpha = alpha_0  # initial step size

    min_theta, min_value = None, float("inf")  # the minimum so far
    iterations_with_no_improvement = 0

    # if we ever go 100 iterations with no improvement, stop
    while iterations_with_no_improvement < 100:

        value = sum(target_fn(x_i, y_i, theta) for x_i, y_i in data)

        if value < min_value:
            # if we've found a new minimum, remember it
            # and go back to the original step size
            min_theta, min_value = theta, value
            iterations_with_no_improvement = 0
            alpha = alpha_0
        else:
            # otherwise we're not improving, so try shrinking the step size
            iterations_with_no_improvement += 1
            alpha *= 0.9

        # and take a gradient step for each of the data points
        for x_i, y_i in in_random_order(data):
            gradient_i = gradient_fn(x_i, y_i, theta)
            theta = vector_subtract(theta, scalar_multiply(alpha, gradient_i))

    return min_theta


def maximize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
    return minimize_stochastic(negate(target_fn), negate_all(gradient_fn), x, y, theta_0, alpha_0)


# step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]

# def minimize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
#     """
#     use gradient descent to find theta that minimizes target function
#     """
#     theta = theta_0  # set theta to initial value
#
#     target_fn = safe(target_fn)  # safe version of target_fn
#     value = target_fn(theta)  # value we're minimizing
#
#     while True:
#         gradient = gradient_fn(theta)
#         next_thetas = [step(theta, gradient, -step_size) for step_size in step_sizes]
#
#         # choose the one that minimizes the error function
#         next_theta = min(next_thetas, key=target_fn)
#         next_value = target_fn(next_theta)
#
#         # stop if we're "converging"
#         if abs(value - next_value) < tolerance:
#             return theta
#         else:
#             theta, value = next_theta, next_value
#
#
# def step(x_values, gradient_values, step_size):
#     new_x = []
#
#     for x_value, gradient_value in zip(x_values, gradient_values):
#         try:
#             new_x.append(x_value + step_size * gradient_value)
#         except OverflowError:
#             new_x.append(float('inf'))
#
#     return new_x
#
#
# def safe(f):
#     def safe_f(*args, **kwargs):
#         try:
#             return f(*args, **kwargs)
#         except:
#             return float('inf')
#
#     return safe_f
#
#
# def maximize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
#     return minimize_batch(negate(target_fn), negate_all(gradient_fn), theta_0, tolerance)


def negate(f):
    """return a function that for any input x returns -f(x)"""
    return lambda *args, **kwargs: -f(*args, **kwargs)


def negate_all(f):
    """the same when f returns a list of numbers"""
    return lambda *args, **kwargs: [-y for y in f(*args, **kwargs)]


def in_random_order(data):
    indexes = [i for i, _ in enumerate(data)]
    random.shuffle(indexes)

    for i in indexes:
        yield data[i]



