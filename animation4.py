from manim import *


class Pendulum(Animation):
    def __init__(self, mobject, **kwargs):
        self.mobject = mobject
        super().__init__(mobject, **kwargs)

    def begin(self) -> None:
        arrow = Line(UP, DOWN)
        arrow.position_tip = self.arrow.get_end()
        self.arrow = arrow
        return super().begin()

    def interpolate_mobject(self, alpha):
        alpha = self.rate_func(alpha)
        self.mobject.move_to(self.arrow.get_end())
        self.arrow.rotate(np.arcsin(alpha))
        return super().interpolate_mobject(alpha)


class test(Scene):
    def construct(self):
        circle = Circle()
        self.play(Pendulum(circle))
        self.wait()
