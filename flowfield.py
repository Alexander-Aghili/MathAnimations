from manim import *

class FlowField(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[0]) * UR + np.cos(pos[1]) * LEFT + pos / 5
        stream_lines = StreamLines(
            func, x_range=[-3, 3, 0.2], y_range=[-2, 2, 0.2], padding=1
        )

        self.play(stream_lines.create())
        self.wait()