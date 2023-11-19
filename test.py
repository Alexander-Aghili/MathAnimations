from manim import *
import math
import numpy as np
import sympy as sp

# define symbolic variable t
t = sp.symbols('t')

def differentiate(func, order):
    """
    recursively find symbolic derivatives
    func: symbolic function to differentiate
    order: highest order derivative (integer)
    """

    # check if highest order derivative is reached
    if order == 0:
        return func

    # differentiate function
    derivative = func.diff(t)

    # recursive call to find next derivative
    return differentiate(derivative, order - 1)



def taylor_series(func, count, point):
    """
    Calculate the Taylor Series for a function at a point to a given approximation.
    func: symbolic function
    count: approximation order
    point: point of expansion
    """

    # Calculate the terms of the Taylor series
    series_terms = [differentiate(func, i).subs(t, point) / math.factorial(i) * (t - point)**i for i in range(count + 1)]

    # Sum the series terms
    taylor_series_result = sum(series_terms)

    return taylor_series_result

# Example usage:
# Define a symbolic function, e.g., sin(t)
func = sp.cos(t)

# Choose the point of expansion, e.g., t=0
expansion_point = 0

# Choose the approximation order, e.g., count=4
approximation_order = 5

# Calculate the Taylor Series
taylor_result = taylor_series(func, approximation_order, expansion_point)

evaluation_point = 0

result_at_evaluation_point = taylor_result.subs(t, evaluation_point)

# Print the result
print(result_at_evaluation_point)