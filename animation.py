from manim import *

config.background_color = WHITE


class circle(Scene):
    def construct(self):
        ax = Axes(x_range=[-4, 4], y_range=[-4, 4])
        ax.set_color(BLACK)
        curve = ax.plot(lambda x: x**2, color=RED)
        area = ax.get_area(curve, [-2, 2])
        self.add(ax)
        self.play(Create(curve), run_time=2)
        self.play(Create(area), run_time=2)
        self.wait(2)
