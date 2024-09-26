from manim import *

config.background_color = WHITE


class FallDown(Animation):
    def __init__(self, mobject, speed=1, **kwargs):
        self.speed = speed
        super().__init__(mobject, **kwargs)

    def interpolate_mobject(self, alpha: float):
        self.mobject.shift(DOWN*self.speed*alpha)

        return super().interpolate_mobject(alpha)


config.background_color = WHITE


class Test(Scene):
    def construct(self):
        circle = Circle()
        circle.shift(UP*2)
        self.add(circle)
        self.play(FallDown(circle, speed=0.1), run_time=5)
