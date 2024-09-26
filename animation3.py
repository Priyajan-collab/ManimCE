from manim import *


class DropObject(Animation):
    # without starting coordinates
    def __init__(self, mobject, **kwargs):
        super().__init__(mobject, **kwargs)
        # self.position = position

    def begin(self):
        # self.mobject = self.mobject.shift(self.position)
        self.mobject.get_center = self.mobject.get_center()

        return super().begin()

    def clean_up_from_scene(self, scene: "Scene") -> None:
        return super().clean_up_from_scene(scene)

    def interpolate_mobject(self, alpha):
        alpha = self.rate_func(alpha)
        # center = self.mobject.get_center
        # self.mobject.shift(2*(1-alpha))


class Test(Scene):
    def construct(self):
        circle = Circle()
        self.add(circle)
        # self.play(circle.animate.shift(2*UP))
        self.wait()
        self.play(DropObject(circle))
