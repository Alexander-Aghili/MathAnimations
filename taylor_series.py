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

def evalAtPoint(x, func):
    return func.subs(t, x)

class TaylorSeries(Scene):

    def play_scene(self, obj):
        self.play(Create(obj), run_time=3)
        self.wait(.5)
        self.play(FadeOut(obj), run_time=1)
        self.remove()


    def construct(self):
        function_np = np.arctan
        function_sp = sp.atan(t)

        axes = Axes(
            x_range=[-10, 10, 1],
            y_range=[-PI/2, PI/2, 1],
            x_length=10,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_with_elongated_ticks": np.arange(0, 100, 10),
            },
            tips=False,
        )
        axes_labels = axes.get_axis_labels()
        sin_graph = axes.plot(lambda x: function_np(x), color=BLUE)


        s1 = axes.plot(lambda x: evalAtPoint(x, taylor_series(function_sp, 0, 0)), color=YELLOW)
        s2 = axes.plot(lambda x: evalAtPoint(x, taylor_series(function_sp, 2, 0)), color=YELLOW_A)
        s3 = axes.plot(lambda x: evalAtPoint(x, taylor_series(function_sp, 4, 0)), color=YELLOW_B)
        s4 = axes.plot(lambda x: evalAtPoint(x, taylor_series(function_sp, 6, 0)), color=YELLOW_C)
        s5 = axes.plot(lambda x: evalAtPoint(x, taylor_series(function_sp, 8, 0)), color=YELLOW_D)
        

        
        labels = VGroup(axes_labels)

        self.play(Create(axes), run_time=1)
        self.add(labels)
        self.play(Create(sin_graph), run_time=3)
        self.play_scene(s1)
        self.play_scene(s2)
        self.play_scene(s3)
        self.play_scene(s4)
        self.play_scene(s5)