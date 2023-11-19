from manim import *

def sin_1(x):
    return 0

def sin_2(x):
    return x

def sin_3(x):
    return sin_2(x) -(pow(x, 3) / 6)

def sin_4(x):
    return sin_3(x) + (pow(x, 5) / 120)

def sin_5(x):
    return sin_4(x) - (pow(x, 7) / 5040)


class TaylorSeries(Scene):
    def play_scene(self, obj):
        self.play(Create(obj), run_time=3)
        self.wait(.5)
        self.play(FadeOut(obj), run_time=1)
        self.remove()


    def construct(self):
        axes = Axes(
            x_range=[-2*PI, 2*PI, PI / 2],
            y_range=[-1.5, 1.5, 1],
            x_length=10,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_with_elongated_ticks": np.arange(-2*PI, 2*PI, PI/2),
            },
            tips=False,
        )
        axes_labels = axes.get_axis_labels()
        sin_graph = axes.plot(lambda x: np.sin(x), color=BLUE)
        s1 = axes.plot(sin_1, color=YELLOW)
        s2 = axes.plot(sin_2, color=YELLOW_A)
        s3 = axes.plot(sin_3, color=YELLOW_B)
        s4 = axes.plot(sin_4, color=YELLOW_C)
        s5 = axes.plot(sin_5, color=YELLOW_D)
        

        
        labels = VGroup(axes_labels)

        self.play(Create(axes), run_time=1)
        self.add(labels)
        self.play(Create(sin_graph), run_time=3)
        self.play_scene(s1)
        self.play_scene(s2)
        self.play_scene(s3)
        self.play_scene(s4)
        self.play_scene(s5)