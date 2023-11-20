from manim import *
import math
import numpy as np
import sympy as sp


# define symbolic variable t
t = sp.symbols('x')


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


#TODO:
#Actually make taylor expansion writing look good
class TaylorSeries(Scene):
    text = None
    grouping = None
    
    def play_scene(self, obj, func_latex, order):
        latex_string = "T_{0}(x) = ".format(order)
        self.text = MathTex(latex_string, func_latex)
        self.text.to_edge(UP)
        self.play(Write(self.text))
        self.play(Create(obj), run_time=3)
        self.wait(.5)
        self.play(FadeOut(obj), run_time=1)
        self.play(FadeOut(self.text), run_time=1)
        self.remove(obj)


    def construct(self):
        xrange=[0.1, 5, 1]
        yrange=[0, 10, 1]
        increment=[0,1,2,3,4]
        config = [MathTex("f(x) = \\sqrt{x}"), 
          lambda x: math.sqrt(x), sp.sqrt(t), 1, 
          xrange, yrange, 
          np.arange(xrange[0], xrange[1], xrange[2])]

        self.text = config[0]
        function_np = config[1]
        function_sp = config[2]
        point = config[3]

        axes = Axes(
            x_range=config[4],
            y_range=config[5],
            x_length=10,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_with_elongated_ticks": config[6],
            },
            tips=False,
        )
        graph = axes.plot(lambda x: function_np(x), color=BLUE)
        self.grouping = VGroup(axes, graph)
        VGroup(self.text, self.grouping).arrange(DOWN)

        self.play(Write(self.text))
        self.play(Create(axes), run_time=1)
        self.play(Create(graph), run_time=3)
        self.play(FadeOut(self.text))

        listfunc=[{"func": taylor_series(function_sp, increment[0], point), "color":YELLOW}, 
                  {"func": taylor_series(function_sp, increment[1], point), "color":YELLOW_A},
                  {"func": taylor_series(function_sp, increment[2], point), "color":YELLOW_B},
                  {"func": taylor_series(function_sp, increment[3], point), "color":YELLOW_C},
                  {"func": taylor_series(function_sp, increment[4], point), "color":YELLOW_D}]
        
        for i in range(len(listfunc)):
            func = listfunc[i]
            s = axes.plot(lambda x: evalAtPoint(x, func['func']), color=func['color'])
            self.play_scene(s, sp.latex(func['func']), i)