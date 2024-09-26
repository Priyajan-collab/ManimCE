from mimetypes import init
from os import remove
from manim import *


class Dispersion(Animation):
    def __init__(self, mobject, dot_radius=0.5, dot_numbers=100, **kwargs):
        super().__init__(mobject, **kwargs)
        self.dot_radius = dot_radius
        self.dot_numbers = dot_numbers

    def begin(self):
        dots = VGroup(
            *[Dot(radius=self.dot_radius).move_to(self.mobject.point_from_proportion(p))
              for p in np.linspace(0, 1, self.dot_numbers)]
        )
        for dot in dots:
            dot.initial_position = dot.get_center()
            dot.shift_vector = 2*(dot.get_center()-self.mobject.get_center())

        dots.set_opacity(0)
        self.mobject.add(dots)
        self.dots = dots
        return super().begin()

    def clean_up_from_scene(self, scene: "Scene") -> None:
        return super().clean_up_from_scene(scene)
        Scene.remove(self.dots)

    def interpolate_mobject(self, alpha):
        # alpha = self.rate_func(alpha)
        if alpha <= 0.5:
            self.mobject.set_opacity(1-alpha*2)
            self.dots.set_opacity(2*(alpha))
        else:
            self.mobject.set_opacity(0)
            self.dots.set_opacity(2*(1-alpha))
            for dot in self.dots:
                dot.move_to(dot.initial_position+2 *
                            (alpha-0.5)*dot.shift_vector)


class Test(Scene):
    def construct(self):
        circle = Circle()
        self.add(circle)
        self.wait()
        self.play(Dispersion(circle, dot_radius=0.05,
                  dot_numbers=100), run_time=3)
        self.wait(4)
